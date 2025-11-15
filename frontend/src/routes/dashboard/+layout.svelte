<script lang="ts">
	/**
	 * Dashboard Layout
	 *
	 * Protected layout with sidebar navigation
	 * Redirects to login if user is not authenticated
	 */

	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { fade, fly } from 'svelte/transition';
	import { authStore } from '$lib/stores/auth';
	import { sidebarStore } from '$lib/stores/sidebar';
	import Sidebar from '$lib/components/Sidebar.svelte';

	let { children } = $props();

	// Initialize auth and check authentication
	onMount(() => {
		authStore.init();
		sidebarStore.init();

		if (!$authStore.isAuthenticated) {
			goto('/login');
		}
	});

	// Get current path for sidebar active state
	let currentPath = $derived($page.url.pathname);

	// Calculate main content margin based on sidebar state
	let sidebarWidth = $derived($sidebarStore.isCollapsed ? 72 : 280);
</script>

<svelte:head>
	<title>Dashboard - ProjectFlow</title>
</svelte:head>

{#if $authStore.isAuthenticated}
	<div class="dashboard-layout">
		<div in:fly={{ x: -280, duration: 300 }}>
			<Sidebar {currentPath} />
		</div>

		<main class="main-content" style="margin-left: {sidebarWidth}px" in:fade={{ duration: 300, delay: 150 }}>
			{@render children()}
		</main>
	</div>
{:else}
	<!-- Loading state while redirecting -->
	<div class="loading-container" in:fade={{ duration: 200 }}>
		<p>Authenticating...</p>
	</div>
{/if}

<style>
	.dashboard-layout {
		display: flex;
		min-height: 100vh;
		background-color: var(--color-background);
	}

	.main-content {
		flex: 1;
		padding: var(--spacing-8);
		min-height: 100vh;
		transition: margin-left var(--transition-base);
	}

	.loading-container {
		min-height: 100vh;
		display: flex;
		align-items: center;
		justify-content: center;
		color: var(--color-text-secondary);
	}

	/* Responsive */
	@media (max-width: 768px) {
		.main-content {
			margin-left: 0;
			padding: var(--spacing-4);
		}

		/* TODO: Add mobile menu toggle */
	}
</style>
