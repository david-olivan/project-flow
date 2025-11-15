<script lang="ts">
	/**
	 * ProjectCard Component
	 *
	 * Displays project information in a card format
	 */

	import type { Project } from '$lib/types';

	interface ProjectCardProps {
		project: Project;
	}

	let { project }: ProjectCardProps = $props();

	// Calculate progress percentage
	let progress = $derived(
		project.taskCount > 0 ? Math.round((project.completedTasks / project.taskCount) * 100) : 0
	);

	// Format date
	function formatDate(dateString: string): string {
		const date = new Date(dateString);
		return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
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

	// TODO: Make functional - navigate to project detail page
	function handleClick() {
		console.log('Project clicked:', project.id, '- TODO: navigate to project detail');
	}

	function handleKeyDown(event: KeyboardEvent) {
		if (event.key === 'Enter' || event.key === ' ') {
			event.preventDefault();
			handleClick();
		}
	}
</script>

<!-- TODO: Make functional - navigate to project detail page -->
<button class="project-card" onclick={handleClick} onkeydown={handleKeyDown}>
	<div class="card-header">
		<h3 class="project-name">{project.name}</h3>
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
	</div>

	<div class="progress-bar">
		<div class="progress-fill" style="width: {progress}%"></div>
	</div>

	<div class="card-footer">
		<span class="footer-text">Updated {formatDate(project.updatedAt)}</span>
	</div>
</button>

<style>
	.project-card {
		width: 100%;
		text-align: left;
		background-color: var(--color-surface-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-card);
		padding: var(--spacing-6);
		box-shadow: var(--shadow-sm);
		transition: var(--transition-all);
		cursor: pointer;
		display: flex;
		flex-direction: column;
		gap: var(--spacing-4);
	}

	.project-card:hover {
		transform: translateY(-2px);
		box-shadow: var(--shadow-lg);
		border-color: var(--color-primary-300);
	}

	.project-card:focus {
		outline: 2px solid var(--color-primary-500);
		outline-offset: 2px;
	}

	/* Header */
	.card-header {
		display: flex;
		justify-content: space-between;
		align-items: flex-start;
		gap: var(--spacing-3);
	}

	.project-name {
		font-size: var(--font-size-xl);
		font-weight: var(--font-weight-semibold);
		color: var(--color-text-primary);
		margin: 0;
		flex: 1;
	}

	/* Status Badge */
	.status-badge {
		padding: var(--spacing-1) var(--spacing-3);
		border-radius: var(--radius-full);
		font-size: var(--font-size-xs);
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

	/* Description */
	.project-description {
		color: var(--color-text-secondary);
		font-size: var(--font-size-sm);
		line-height: var(--line-height-relaxed);
		margin: 0;
	}

	/* Stats */
	.project-stats {
		display: flex;
		gap: var(--spacing-6);
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
		font-size: var(--font-size-lg);
		font-weight: var(--font-weight-semibold);
		color: var(--color-text-primary);
	}

	/* Progress Bar */
	.progress-bar {
		width: 100%;
		height: 6px;
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

	/* Footer */
	.card-footer {
		padding-top: var(--spacing-3);
		border-top: 1px solid var(--color-border);
	}

	.footer-text {
		font-size: var(--font-size-xs);
		color: var(--color-text-tertiary);
	}
</style>
