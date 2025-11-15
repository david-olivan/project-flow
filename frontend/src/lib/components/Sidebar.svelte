<script lang="ts">
	/**
	 * Sidebar Component - Dashboard Navigation
	 *
	 * Main navigation sidebar for the dashboard
	 */

	import { authStore } from '$lib/stores/auth';
	import Logo from './Logo.svelte';

	interface SidebarProps {
		currentPath?: string;
	}

	let { currentPath = '' }: SidebarProps = $props();

	function handleLogout() {
		authStore.logout();
	}

	// TODO: Make functional - connect to project creation flow
	function handleNewProject() {
		console.log('New Project clicked - TODO: implement project creation');
	}

	// TODO: Make functional - connect to projects list view
	function handleAllProjects() {
		console.log('All Projects clicked - TODO: implement projects list');
	}

	// TODO: Make functional - connect to profile settings
	function handleProfile() {
		console.log('Profile clicked - TODO: implement profile settings');
	}

	let user = $derived($authStore.user);
</script>

<aside class="sidebar">
	<!-- Top Section: Logo & Brand -->
	<div class="sidebar-header">
		<Logo size="md" />
	</div>

	<!-- Main Navigation -->
	<nav class="sidebar-nav">
		<ul class="nav-list">
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

			<!-- TODO: Make functional - connect to projects list view -->
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
		</ul>
	</nav>

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

		<button class="footer-item logout" onclick={handleLogout} aria-label="Logout">
			<svg class="footer-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
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
	}

	/* Header */
	.sidebar-header {
		padding: var(--spacing-6);
		border-bottom: 1px solid var(--color-border);
	}

	/* Navigation */
	.sidebar-nav {
		flex: 1;
		padding: var(--spacing-4);
		overflow-y: auto;
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
		gap: var(--spacing-3);
		width: 100%;
		padding: var(--spacing-3) var(--spacing-4);
		background: transparent;
		border: none;
		border-radius: var(--radius-lg);
		color: var(--color-text-secondary);
		font-size: var(--font-size-base);
		font-weight: var(--font-weight-medium);
		cursor: pointer;
		transition: var(--transition-colors);
		text-align: left;
	}

	.nav-item:hover {
		background-color: var(--color-primary-50);
		color: var(--color-primary-700);
	}

	[data-theme='dark'] .nav-item:hover {
		background-color: var(--color-primary-900);
		color: var(--color-primary-300);
	}

	.nav-item.active {
		background-color: var(--color-primary-100);
		color: var(--color-primary-700);
	}

	[data-theme='dark'] .nav-item.active {
		background-color: var(--color-primary-800);
		color: var(--color-primary-300);
	}

	.nav-icon {
		width: 20px;
		height: 20px;
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
		gap: var(--spacing-3);
		width: 100%;
		padding: var(--spacing-3) var(--spacing-4);
		background: transparent;
		border: none;
		border-radius: var(--radius-lg);
		color: var(--color-text-secondary);
		font-size: var(--font-size-sm);
		font-weight: var(--font-weight-medium);
		cursor: pointer;
		transition: var(--transition-colors);
		text-align: left;
	}

	.footer-item:hover {
		background-color: var(--color-neutral-100);
		color: var(--color-text-primary);
	}

	[data-theme='dark'] .footer-item:hover {
		background-color: var(--color-neutral-800);
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
		flex-shrink: 0;
	}

	.footer-text {
		font-size: var(--font-size-sm);
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
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
		.sidebar.open {
			transform: translateX(0);
		}
	}
</style>
