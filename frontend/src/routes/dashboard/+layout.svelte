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
	import { authStore } from '$lib/stores/auth';
	import Sidebar from '$lib/components/Sidebar.svelte';

	// Initialize auth and check authentication
	onMount(() => {
		authStore.init();

		if (!$authStore.isAuthenticated) {
			goto('/login');
		}
	});

	// Get current path for sidebar active state
	let currentPath = $derived($page.url.pathname);
</script>

<svelte:head>
	<title>Dashboard - ProjectFlow</title>
</svelte:head>

{#if $authStore.isAuthenticated}
	<div class="dashboard-layout">
		<Sidebar {currentPath} />

		<main class="main-content">
			<slot />
		</main>
	</div>
{:else}
	<!-- Loading state while redirecting -->
	<div class="loading-container">
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
		margin-left: 280px; /* Width of sidebar */
		padding: var(--spacing-8);
		min-height: 100vh;
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
