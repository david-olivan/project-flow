<script lang="ts">
	/**
	 * Project Detail Page
	 *
	 * Displays project information and associated tasks
	 */

	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { fade, fly } from 'svelte/transition';
	import type { Project, Task } from '$lib/types';
	import TaskCard from '$lib/components/TaskCard.svelte';

	let project = $state<Project | null>(null);
	let tasks = $state<Task[]>([]);
	let isLoading = $state(true);
	let error = $state('');

	let projectId = $derived($page.params.id);

	onMount(async () => {
		await loadProjectData();
	});

	async function loadProjectData() {
		try {
			isLoading = true;
			error = '';

			// TODO (TECH DEBT): Replace with actual API calls
			// Load project data
			const projectsResponse = await fetch('/mock_data/projects.json');
			if (!projectsResponse.ok) {
				throw new Error('Failed to load project');
			}
			const projectsData = await projectsResponse.json();
			const foundProject = projectsData.projects.find((p: Project) => p.id === projectId);

			if (!foundProject) {
				throw new Error('Project not found');
			}

			project = foundProject;

			// Load tasks for this project
			const tasksResponse = await fetch('/mock_data/tasks.json');
			if (!tasksResponse.ok) {
				throw new Error('Failed to load tasks');
			}
			const tasksData = await tasksResponse.json();
			tasks = tasksData.tasks.filter((t: Task) => t.belongs_to === projectId);
		} catch (err) {
			error = err instanceof Error ? err.message : 'Failed to load project';
			console.error('Error loading project data:', err);
		} finally {
			isLoading = false;
		}
	}

	// Get status color
	function getStatusColor(status: Project['status']): string {
		const colors = {
			planning: 'status-planning',
			in_progress: 'status-in-progress',
			completed: 'status-completed',
			on_hold: 'status-on-hold'
		};
		return colors[status] || '';
	}

	// Format status text
	function formatStatus(status: Project['status']): string {
		return status.replace('_', ' ').replace(/\b\w/g, (l) => l.toUpperCase());
	}

	// Calculate progress
	let progress = $derived(
		project && project.taskCount > 0
			? Math.round((project.completedTasks / project.taskCount) * 100)
			: 0
	);
</script>

<div class="project-detail-page">
	<!-- Loading State -->
	{#if isLoading}
		<div class="loading-state" in:fade={{ duration: 200 }}>
			<div class="loading-spinner"></div>
			<p>Loading project...</p>
		</div>
	{/if}

	<!-- Error State -->
	{#if error && !isLoading}
		<div class="error-state" in:fade={{ duration: 200 }}>
			<p class="error-message">{error}</p>
			<a href="/dashboard" class="back-link">Back to Dashboard</a>
		</div>
	{/if}

	<!-- Project Content -->
	{#if !isLoading && !error && project}
		<!-- Project Header -->
		<header class="project-header" in:fade={{ duration: 300, delay: 100 }}>
			<div class="header-top">
				<div>
					<h1 class="project-title">{project.name}</h1>
					<p class="project-team">{project.team}</p>
				</div>
				<span class="status-badge {getStatusColor(project.status)}">
					{formatStatus(project.status)}
				</span>
			</div>

			<p class="project-description">{project.description}</p>

			<div class="project-stats">
				<div class="stat">
					<span class="stat-label">Tasks</span>
					<span class="stat-value">{project.completedTasks}/{project.taskCount}</span>
				</div>

				<div class="stat">
					<span class="stat-label">Progress</span>
					<span class="stat-value">{progress}%</span>
				</div>

				<div class="stat">
					<span class="stat-label">Total Tasks</span>
					<span class="stat-value">{tasks.length}</span>
				</div>
			</div>

			<div class="progress-bar">
				<div class="progress-fill" style="width: {progress}%"></div>
			</div>
		</header>

		<!-- Tasks Section -->
		<section class="tasks-section">
			<h2 class="section-title">Tasks</h2>

			{#if tasks.length === 0}
				<div class="empty-state" in:fade={{ duration: 200 }}>
					<svg
						class="empty-icon"
						viewBox="0 0 24 24"
						fill="none"
						xmlns="http://www.w3.org/2000/svg"
					>
						<rect x="3" y="3" width="18" height="18" rx="2" stroke="currentColor" stroke-width="2" />
						<path d="M9 11l2 2 4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
					</svg>
					<p class="empty-text">No tasks yet for this project</p>
				</div>
			{:else}
				<div class="tasks-grid">
					{#each tasks as task, index (task.id)}
						<div in:fly={{ y: 20, duration: 300, delay: 100 + index * 30 }}>
							<TaskCard {task} />
						</div>
					{/each}
				</div>
			{/if}
		</section>
	{/if}
</div>

<style>
	.project-detail-page {
		width: 100%;
		max-width: 1400px;
		margin: 0 auto;
	}

	/* Loading State */
	.loading-state {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: var(--spacing-20);
		gap: var(--spacing-4);
		color: var(--color-text-secondary);
	}

	.loading-spinner {
		width: 48px;
		height: 48px;
		border: 4px solid var(--color-primary-200);
		border-top-color: var(--color-primary-600);
		border-radius: 50%;
		animation: spin 0.8s linear infinite;
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
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

	.back-link {
		color: var(--color-primary-600);
		text-decoration: none;
		font-weight: var(--font-weight-medium);
		transition: var(--transition-base);
	}

	.back-link:hover {
		color: var(--color-primary-700);
		text-decoration: underline;
	}

	/* Project Header */
	.project-header {
		background-color: var(--color-surface-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-card);
		padding: var(--spacing-8);
		margin-bottom: var(--spacing-8);
		box-shadow: var(--shadow-sm);
	}

	.header-top {
		display: flex;
		justify-content: space-between;
		align-items: flex-start;
		gap: var(--spacing-4);
		margin-bottom: var(--spacing-4);
	}

	.project-title {
		font-size: var(--font-size-4xl);
		font-weight: var(--font-weight-bold);
		color: var(--color-text-primary);
		margin: 0 0 var(--spacing-2) 0;
	}

	.project-team {
		font-size: var(--font-size-base);
		color: var(--color-text-secondary);
		margin: 0;
	}

	/* Status Badge */
	.status-badge {
		padding: var(--spacing-2) var(--spacing-4);
		border-radius: var(--radius-full);
		font-size: var(--font-size-sm);
		font-weight: var(--font-weight-medium);
		text-transform: capitalize;
		white-space: nowrap;
	}

	.status-planning {
		background-color: var(--color-neutral-100);
		color: var(--color-neutral-700);
	}

	.status-in-progress {
		background-color: var(--color-accent-100);
		color: var(--color-accent-700);
	}

	.status-completed {
		background-color: rgba(34, 197, 94, 0.1);
		color: var(--color-success);
	}

	.status-on-hold {
		background-color: rgba(245, 158, 11, 0.1);
		color: var(--color-warning);
	}

	.project-description {
		color: var(--color-text-secondary);
		font-size: var(--font-size-base);
		line-height: var(--line-height-relaxed);
		margin: 0 0 var(--spacing-6) 0;
	}

	/* Stats */
	.project-stats {
		display: flex;
		gap: var(--spacing-8);
		margin-bottom: var(--spacing-6);
	}

	.stat {
		display: flex;
		flex-direction: column;
		gap: var(--spacing-1);
	}

	.stat-label {
		font-size: var(--font-size-xs);
		color: var(--color-text-tertiary);
		text-transform: uppercase;
		letter-spacing: var(--letter-spacing-wide);
	}

	.stat-value {
		font-size: var(--font-size-2xl);
		font-weight: var(--font-weight-semibold);
		color: var(--color-text-primary);
	}

	/* Progress Bar */
	.progress-bar {
		width: 100%;
		height: 8px;
		background-color: var(--color-neutral-200);
		border-radius: var(--radius-full);
		overflow: hidden;
	}

	.progress-fill {
		height: 100%;
		background: linear-gradient(90deg, var(--color-primary-600), var(--color-accent-500));
		border-radius: var(--radius-full);
		transition: width var(--transition-slow);
	}

	/* Tasks Section */
	.tasks-section {
		margin-bottom: var(--spacing-8);
	}

	.section-title {
		font-size: var(--font-size-2xl);
		font-weight: var(--font-weight-semibold);
		color: var(--color-text-primary);
		margin: 0 0 var(--spacing-6) 0;
	}

	.tasks-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
		gap: var(--spacing-4);
	}

	/* Empty State */
	.empty-state {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: var(--spacing-16);
		text-align: center;
		gap: var(--spacing-4);
	}

	.empty-icon {
		width: 64px;
		height: 64px;
		color: var(--color-text-tertiary);
		margin-bottom: var(--spacing-2);
	}

	.empty-text {
		font-size: var(--font-size-base);
		color: var(--color-text-secondary);
		margin: 0;
	}

	/* Responsive */
	@media (max-width: 768px) {
		.project-header {
			padding: var(--spacing-6);
		}

		.project-title {
			font-size: var(--font-size-3xl);
		}

		.header-top {
			flex-direction: column;
			align-items: flex-start;
		}

		.project-stats {
			flex-wrap: wrap;
			gap: var(--spacing-6);
		}

		.tasks-grid {
			grid-template-columns: 1fr;
		}

		.stat-value {
			font-size: var(--font-size-xl);
		}
	}
</style>
