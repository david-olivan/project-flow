<script lang="ts">
	/**
	 * Dashboard Home Page
	 *
	 * Displays user's projects in a grid
	 */

	import { onMount } from 'svelte';
	import type { Project } from '$lib/types';
	import ProjectCard from '$lib/components/ProjectCard.svelte';

	let projects = $state<Project[]>([]);
	let isLoading = $state(true);
	let error = $state('');

	onMount(async () => {
		await loadProjects();
	});

	async function loadProjects() {
		try {
			isLoading = true;
			error = '';

			// TODO (TECH DEBT): Replace with actual API call
			// const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/api/projects`, {
			//   headers: { 'Authorization': `Bearer ${apiKey}` }
			// });

			// Load mock data from static folder
			const response = await fetch('/mock_data/projects.json');

			if (!response.ok) {
				throw new Error('Failed to load projects');
			}

			const data = await response.json();
			projects = data.projects;
		} catch (err) {
			error = 'Failed to load projects. Please try again.';
			console.error('Error loading projects:', err);
		} finally {
			isLoading = false;
		}
	}
</script>

<div class="dashboard-page">
	<!-- Page Header -->
	<header class="page-header">
		<div>
			<h1 class="page-title">Projects</h1>
			<p class="page-subtitle">Manage and track all your projects in one place</p>
		</div>
	</header>

	<!-- Loading State -->
	{#if isLoading}
		<div class="loading-state">
			<p>Loading projects...</p>
		</div>
	{/if}

	<!-- Error State -->
	{#if error && !isLoading}
		<div class="error-state">
			<p class="error-message">{error}</p>
			<button class="retry-button" onclick={loadProjects}>Try Again</button>
		</div>
	{/if}

	<!-- Empty State -->
	{#if !isLoading && !error && projects.length === 0}
		<div class="empty-state">
			<svg
				class="empty-icon"
				viewBox="0 0 24 24"
				fill="none"
				xmlns="http://www.w3.org/2000/svg"
			>
				<rect
					x="3"
					y="3"
					width="18"
					height="18"
					rx="2"
					stroke="currentColor"
					stroke-width="2"
				/>
				<line x1="12" y1="8" x2="12" y2="16" stroke="currentColor" stroke-width="2" />
				<line x1="8" y1="12" x2="16" y2="12" stroke="currentColor" stroke-width="2" />
			</svg>
			<h2 class="empty-title">No projects yet</h2>
			<p class="empty-description">Get started by creating your first project</p>
			<!-- TODO: Make functional - connect to project creation flow -->
			<button class="empty-cta">Create Project</button>
		</div>
	{/if}

	<!-- Projects Grid -->
	{#if !isLoading && !error && projects.length > 0}
		<div class="projects-grid">
			{#each projects as project (project.id)}
				<ProjectCard {project} />
			{/each}
		</div>
	{/if}
</div>

<style>
	.dashboard-page {
		width: 100%;
		max-width: 1400px;
		margin: 0 auto;
	}

	/* Page Header */
	.page-header {
		margin-bottom: var(--spacing-8);
		display: flex;
		justify-content: space-between;
		align-items: flex-start;
	}

	.page-title {
		font-size: var(--font-size-4xl);
		font-weight: var(--font-weight-bold);
		color: var(--color-text-primary);
		margin: 0 0 var(--spacing-2) 0;
	}

	.page-subtitle {
		font-size: var(--font-size-base);
		color: var(--color-text-secondary);
		margin: 0;
	}

	/* Loading State */
	.loading-state {
		display: flex;
		align-items: center;
		justify-content: center;
		padding: var(--spacing-20);
		color: var(--color-text-secondary);
	}

	/* Error State */
	.error-state {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: var(--spacing-20);
		gap: var(--spacing-4);
	}

	.error-message {
		color: var(--color-error);
		font-size: var(--font-size-base);
	}

	.retry-button {
		padding: var(--spacing-3) var(--spacing-6);
		background-color: var(--color-primary-600);
		color: var(--color-text-inverse);
		border: none;
		border-radius: var(--radius-button);
		font-weight: var(--font-weight-medium);
		cursor: pointer;
		transition: var(--transition-all);
	}

	.retry-button:hover {
		background-color: var(--color-primary-700);
	}

	/* Empty State */
	.empty-state {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: var(--spacing-20);
		text-align: center;
		gap: var(--spacing-4);
	}

	.empty-icon {
		width: 80px;
		height: 80px;
		color: var(--color-text-tertiary);
		margin-bottom: var(--spacing-4);
	}

	.empty-title {
		font-size: var(--font-size-2xl);
		font-weight: var(--font-weight-semibold);
		color: var(--color-text-primary);
		margin: 0;
	}

	.empty-description {
		font-size: var(--font-size-base);
		color: var(--color-text-secondary);
		margin: 0;
	}

	.empty-cta {
		margin-top: var(--spacing-4);
		padding: var(--spacing-3) var(--spacing-6);
		background-color: var(--color-primary-600);
		color: var(--color-text-inverse);
		border: none;
		border-radius: var(--radius-button);
		font-weight: var(--font-weight-medium);
		cursor: pointer;
		transition: var(--transition-all);
	}

	.empty-cta:hover {
		background-color: var(--color-primary-700);
		transform: translateY(-1px);
		box-shadow: var(--shadow-md);
	}

	/* Projects Grid */
	.projects-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
		gap: var(--spacing-6);
	}

	/* Responsive */
	@media (max-width: 768px) {
		.page-title {
			font-size: var(--font-size-3xl);
		}

		.projects-grid {
			grid-template-columns: 1fr;
		}

		.empty-state,
		.loading-state,
		.error-state {
			padding: var(--spacing-12);
		}
	}
</style>
