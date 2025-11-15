<script lang="ts">
	/**
	 * Sidebar Component - Dashboard Navigation
	 *
	 * Main navigation sidebar for the dashboard
	 */

	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { authStore } from '$lib/stores/auth';
	import { sidebarStore } from '$lib/stores/sidebar';
	import { fade } from 'svelte/transition';
	import Logo from './Logo.svelte';

	interface SidebarProps {
		currentPath?: string;
	}

	let { currentPath = '' }: SidebarProps = $props();
	let isLoggingOut = $state(false);

	// Check if we're on a project detail page
	let isProjectDetailPage = $derived(currentPath.startsWith('/dashboard/projects/'));

	onMount(() => {
		sidebarStore.init();
	});

	async function handleLogout() {
		isLoggingOut = true;

		// Small delay for UX, show logging out state
		await new Promise((resolve) => setTimeout(resolve, 500));

		authStore.logout();
	}

	// TODO: Make functional - connect to project creation flow
	function handleNewProject() {
		console.log('New Project clicked - TODO: implement project creation');
	}

	// Navigate to all projects (dashboard)
	function handleAllProjects() {
		goto('/dashboard');
	}

	// Navigate back from project detail page
	function handleGoBack() {
		goto('/dashboard');
	}

	// TODO: Make functional - connect to profile settings
	function handleProfile() {
		console.log('Profile clicked - TODO: implement profile settings');
	}

	let user = $derived($authStore.user);
</script>

<aside class="sidebar" class:collapsed={$sidebarStore.isCollapsed}>
	<!-- Top Section: Logo & Brand -->
	<div class="sidebar-header">
		<Logo size="md" showIcon={true} showText={!$sidebarStore.isCollapsed} />
	</div>

	<!-- Main Navigation -->
	<nav class="sidebar-nav">
		<ul class="nav-list">
			{#if isProjectDetailPage}
				<!-- Go Back button when on project detail page -->
				<li>
					<button class="nav-item" onclick={handleGoBack} aria-label="Go back to dashboard">
						<svg class="nav-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
							<path
								d="M19 12H5M12 19l-7-7 7-7"
								stroke="currentColor"
								stroke-width="2"
								stroke-linecap="round"
								stroke-linejoin="round"
							/>
						</svg>
						<span>Go Back</span>
					</button>
				</li>
			{:else}
				<!-- Default navigation items -->
				<!-- TODO: Make functional - connect to project creation flow -->
				<li>
					<button class="nav-item" onclick={handleNewProject} aria-label="Create new project">
						<svg class="nav-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
							<path
								d="M12 5v14m-7-7h14"
								stroke="currentColor"
								stroke-width="2"
								stroke-linecap="round"
							/>
						</svg>
						<span>New Project</span>
					</button>
				</li>

				<li>
					<button
						class="nav-item"
						class:active={currentPath === '/dashboard'}
						onclick={handleAllProjects}
						aria-label="View all projects"
					>
						<svg class="nav-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
							<path
								d="M3 7h18M3 12h18M3 17h18"
								stroke="currentColor"
								stroke-width="2"
								stroke-linecap="round"
							/>
						</svg>
						<span>All Projects</span>
					</button>
				</li>
			{/if}
		</ul>
	</nav>

	<!-- Collapse Toggle Button -->
	<div class="sidebar-toggle">
		<button
			class="toggle-button"
			onclick={() => sidebarStore.toggleCollapsed()}
			aria-label={$sidebarStore.isCollapsed ? 'Expand sidebar' : 'Collapse sidebar'}
			title={$sidebarStore.isCollapsed ? 'Expand sidebar' : 'Collapse sidebar'}
		>
			<svg class="toggle-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
				{#if $sidebarStore.isCollapsed}
					<!-- Expand icon (chevrons right) -->
					<path
						d="M13 17l5-5-5-5M6 17l5-5-5-5"
						stroke="currentColor"
						stroke-width="2"
						stroke-linecap="round"
						stroke-linejoin="round"
					/>
				{:else}
					<!-- Collapse icon (chevrons left) -->
					<path
						d="M11 17l-5-5 5-5M18 17l-5-5 5-5"
						stroke="currentColor"
						stroke-width="2"
						stroke-linecap="round"
						stroke-linejoin="round"
					/>
				{/if}
			</svg>
			{#if !$sidebarStore.isCollapsed}
				<span class="toggle-text">Collapse</span>
			{/if}
		</button>
	</div>

	<!-- Bottom Section: User Actions -->
	<div class="sidebar-footer">
		<!-- TODO: Make functional - connect to profile settings -->
		<button class="footer-item" onclick={handleProfile} aria-label="Profile settings">
			<svg class="footer-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
				<circle cx="12" cy="8" r="4" stroke="currentColor" stroke-width="2" />
				<path
					d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2"
					stroke="currentColor"
					stroke-width="2"
					stroke-linecap="round"
				/>
			</svg>
			<span class="footer-text">{user?.username || 'Profile'}</span>
		</button>

		<button
			class="footer-item logout"
			onclick={handleLogout}
			disabled={isLoggingOut}
			aria-label="Logout"
		>
			{#if isLoggingOut}
				<div class="logout-spinner"></div>
				<span class="footer-text">Logging out...</span>
			{:else}
				<svg
					class="footer-icon"
					viewBox="0 0 24 24"
					fill="none"
					xmlns="http://www.w3.org/2000/svg"
				>
					<path
						d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"
						stroke="currentColor"
						stroke-width="2"
						stroke-linecap="round"
					/>
					<polyline
						points="16 17 21 12 16 7"
						stroke="currentColor"
						stroke-width="2"
						stroke-linecap="round"
						stroke-linejoin="round"
					/>
					<line
						x1="21"
						y1="12"
						x2="9"
						y2="12"
						stroke="currentColor"
						stroke-width="2"
						stroke-linecap="round"
					/>
				</svg>
				<span class="footer-text">Logout</span>
			{/if}
		</button>
	</div>
</aside>

<style>
	.sidebar {
		width: 280px;
		height: 100vh;
		background-color: var(--color-surface-elevated);
		border-right: 1px solid var(--color-border);
		display: flex;
		flex-direction: column;
		position: fixed;
		left: 0;
		top: 0;
		z-index: 100;
		transition: width var(--transition-slow), box-shadow var(--transition-base);
		overflow: hidden; /* Prevent any scrollbar during transition */
	}

	/* Hide scrollbar but keep functionality */
	.sidebar::-webkit-scrollbar {
		width: 0px;
		background: transparent;
	}

	.sidebar.collapsed {
		width: 72px;
	}

	/* Header */
	.sidebar-header {
		padding: var(--spacing-6);
		border-bottom: 1px solid var(--color-border);
		display: flex;
		justify-content: flex-start;
	}

	.sidebar.collapsed .sidebar-header {
		justify-content: center;
	}

	/* Navigation */
	.sidebar-nav {
		flex: 1;
		padding: var(--spacing-4);
		overflow-y: auto;
		overflow-x: hidden;
	}

	/* Hide scrollbar for nav section */
	.sidebar-nav::-webkit-scrollbar {
		width: 0px;
		background: transparent;
	}

	.nav-list {
		display: flex;
		flex-direction: column;
		gap: var(--spacing-2);
		list-style: none;
		padding: 0;
		margin: 0;
	}

	.nav-item {
		display: flex;
		align-items: center;
		justify-content: flex-start;
		gap: var(--spacing-3);
		width: 100%;
		padding: var(--spacing-3);
		background: transparent;
		border: none;
		border-radius: var(--radius-lg);
		color: var(--color-text-secondary);
		font-size: var(--font-size-base);
		font-weight: var(--font-weight-medium);
		cursor: pointer;
		transition: all var(--transition-base);
		text-align: left;
		white-space: nowrap;
	}

	.sidebar.collapsed .nav-item {
		justify-content: center;
		padding: var(--spacing-3);
	}

	.sidebar.collapsed .nav-item span {
		display: none;
	}

	.nav-item:hover {
		background-color: var(--color-primary-50);
		color: var(--color-primary-700);
	}

	.nav-item.active {
		background-color: var(--color-primary-100);
		color: var(--color-primary-700);
	}

	.nav-icon {
		width: 20px;
		height: 20px;
		min-width: 20px;
		min-height: 20px;
		flex-shrink: 0;
	}

	/* Footer */
	.sidebar-footer {
		padding: var(--spacing-4);
		border-top: 1px solid var(--color-border);
		display: flex;
		flex-direction: column;
		gap: var(--spacing-2);
	}

	.footer-item {
		display: flex;
		align-items: center;
		justify-content: flex-start;
		gap: var(--spacing-3);
		width: 100%;
		padding: var(--spacing-3);
		background: transparent;
		border: none;
		border-radius: var(--radius-lg);
		color: var(--color-text-secondary);
		font-size: var(--font-size-sm);
		font-weight: var(--font-weight-medium);
		cursor: pointer;
		transition: all var(--transition-base);
		text-align: left;
	}

	.sidebar.collapsed .footer-item {
		justify-content: center;
		padding: var(--spacing-3);
	}

	.footer-item:hover {
		background-color: var(--color-primary-50);
		color: var(--color-primary-700);
	}

	.footer-item.logout {
		color: var(--color-error);
	}

	.footer-item.logout:hover {
		background-color: rgba(239, 68, 68, 0.1);
		color: var(--color-error);
	}

	.footer-icon {
		width: 18px;
		height: 18px;
		min-width: 18px;
		min-height: 18px;
		flex-shrink: 0;
	}

	.footer-text {
		font-size: var(--font-size-sm);
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	}

	.sidebar.collapsed .footer-text {
		display: none;
	}

	.sidebar.collapsed .toggle-text {
		display: none;
	}

	/* Sidebar Toggle */
	.sidebar-toggle {
		padding: var(--spacing-4);
		border-top: 1px solid var(--color-border);
	}

	.toggle-button {
		display: flex;
		align-items: center;
		justify-content: flex-start;
		gap: var(--spacing-3);
		width: 100%;
		padding: var(--spacing-3);
		background: transparent;
		border: none;
		border-radius: var(--radius-lg);
		color: var(--color-text-secondary);
		font-size: var(--font-size-sm);
		font-weight: var(--font-weight-medium);
		cursor: pointer;
		transition: all var(--transition-base);
		text-align: left;
	}

	.sidebar.collapsed .toggle-button {
		justify-content: center;
		padding: var(--spacing-3);
	}

	.toggle-button:hover {
		background-color: var(--color-neutral-100);
		color: var(--color-primary-600);
	}

	.toggle-icon {
		width: 18px;
		height: 18px;
		min-width: 18px;
		min-height: 18px;
		flex-shrink: 0;
	}

	.toggle-text {
		font-size: var(--font-size-sm);
		white-space: nowrap;
	}

	.logout-spinner {
		width: 18px;
		height: 18px;
		border: 2px solid rgba(239, 68, 68, 0.3);
		border-top-color: var(--color-error);
		border-radius: 50%;
		animation: spin 0.6s linear infinite;
		flex-shrink: 0;
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}

	.footer-item:disabled {
		opacity: 0.7;
		cursor: not-allowed;
	}

	/* Responsive */
	@media (max-width: 768px) {
		.sidebar {
			width: 100%;
			max-width: 280px;
			transform: translateX(-100%);
			transition: transform var(--transition-base);
			box-shadow: var(--shadow-2xl);
		}

		/* TODO: Add mobile menu toggle functionality */
	}
</style>
