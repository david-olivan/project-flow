<script lang="ts">
	/**
	 * Root Page - Redirect Logic
	 *
	 * Redirects users to dashboard if authenticated, otherwise to login
	 */

	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { authStore } from '$lib/stores/auth';

	onMount(() => {
		// Initialize auth store
		authStore.init();

		// Redirect based on authentication status
		if ($authStore.isAuthenticated) {
			goto('/dashboard');
		} else {
			goto('/login');
		}
	});
</script>

<svelte:head>
	<title>ProjectFlow</title>
</svelte:head>

<!-- Loading state while redirecting -->
<div class="loading-container">
	<p>Loading...</p>
</div>

<style>
	.loading-container {
		min-height: 100vh;
		display: flex;
		align-items: center;
		justify-content: center;
		color: var(--color-text-secondary);
	}
</style>
