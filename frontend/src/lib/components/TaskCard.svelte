<script lang="ts">
	/**
	 * TaskCard Component
	 *
	 * Displays task information in a card format
	 */

	import type { Task } from '$lib/types';

	interface TaskCardProps {
		task: Task;
	}

	let { task }: TaskCardProps = $props();

	// Format date
	function formatDate(dateString: string | null): string {
		if (!dateString) return 'Not set';
		const date = new Date(dateString);
		return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
	}

	// Get priority color
	function getPriorityColor(priority: Task['priority']): string {
		const colors = {
			low: 'priority-low',
			medium: 'priority-medium',
			high: 'priority-high'
		};
		return colors[priority] || '';
	}

	// Get status color
	function getStatusColor(status: Task['status']): string {
		const colors = {
			pending: 'status-pending',
			in_progress: 'status-in-progress',
			completed: 'status-completed'
		};
		return colors[status] || '';
	}

	// Format status text
	function formatStatus(status: Task['status']): string {
		return status.replace('_', ' ').replace(/\b\w/g, (l) => l.toUpperCase());
	}

	// Format priority text
	function formatPriority(priority: Task['priority']): string {
		return priority.charAt(0).toUpperCase() + priority.slice(1);
	}

	// Format effort hours
	function formatEffort(effort: number | null): string {
		if (effort === null) return 'Not estimated';
		return `${effort}h`;
	}

	// TODO: Make functional - handle task click/edit
	function handleClick() {
		console.log('Task clicked:', task.id, '- TODO: implement task detail/edit');
	}

	function handleKeyDown(event: KeyboardEvent) {
		if (event.key === 'Enter' || event.key === ' ') {
			event.preventDefault();
			handleClick();
		}
	}
</script>

<!-- TODO: Make functional - handle task click/edit -->
<button class="task-card" onclick={handleClick} onkeydown={handleKeyDown}>
	<div class="card-header">
		<div class="header-left">
			<h3 class="task-name">{task.name}</h3>
			<div class="badges">
				<span class="priority-badge {getPriorityColor(task.priority)}">
					{formatPriority(task.priority)}
				</span>
				<span class="status-badge {getStatusColor(task.status)}">
					{formatStatus(task.status)}
				</span>
			</div>
		</div>
	</div>

	{#if task.notes}
		<p class="task-notes">{task.notes}</p>
	{/if}

	<div class="task-metadata">
		<div class="metadata-item">
			<svg class="metadata-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
				<rect x="3" y="4" width="18" height="18" rx="2" stroke="currentColor" stroke-width="2" />
				<line x1="16" y1="2" x2="16" y2="6" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
				<line x1="8" y1="2" x2="8" y2="6" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
				<line x1="3" y1="10" x2="21" y2="10" stroke="currentColor" stroke-width="2" />
			</svg>
			<span class="metadata-text">{formatDate(task.start_date)} - {formatDate(task.end_date)}</span>
		</div>

		<div class="metadata-item">
			<svg class="metadata-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
				<circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" />
				<path d="M12 6v6l4 2" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
			</svg>
			<span class="metadata-text">{formatEffort(task.effort)}</span>
		</div>

		{#if task.assigned_to.length > 0}
			<div class="metadata-item">
				<svg class="metadata-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
					<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
					<circle cx="9" cy="7" r="4" stroke="currentColor" stroke-width="2" />
					<path d="M22 21v-2a4 4 0 0 0-3-3.87" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
					<path d="M16 3.13a4 4 0 0 1 0 7.75" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
				</svg>
				<span class="metadata-text">{task.assigned_to.length} assigned</span>
			</div>
		{/if}
	</div>
</button>

<style>
	.task-card {
		width: 100%;
		text-align: left;
		background-color: var(--color-surface-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-card);
		padding: var(--spacing-5);
		box-shadow: var(--shadow-sm);
		transition: var(--transition-all);
		cursor: pointer;
		display: flex;
		flex-direction: column;
		gap: var(--spacing-3);
	}

	.task-card:hover {
		transform: translateY(-1px);
		box-shadow: var(--shadow-md);
		border-color: var(--color-primary-300);
	}

	.task-card:focus {
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

	.header-left {
		display: flex;
		flex-direction: column;
		gap: var(--spacing-2);
		flex: 1;
	}

	.task-name {
		font-size: var(--font-size-lg);
		font-weight: var(--font-weight-semibold);
		color: var(--color-text-primary);
		margin: 0;
	}

	.badges {
		display: flex;
		gap: var(--spacing-2);
		flex-wrap: wrap;
	}

	/* Priority Badge */
	.priority-badge {
		padding: var(--spacing-1) var(--spacing-2);
		border-radius: var(--radius-full);
		font-size: var(--font-size-xs);
		font-weight: var(--font-weight-medium);
		text-transform: capitalize;
		white-space: nowrap;
	}

	.priority-low {
		background-color: var(--color-neutral-100);
		color: var(--color-neutral-700);
	}

	.priority-medium {
		background-color: var(--color-accent-100);
		color: var(--color-accent-700);
	}

	.priority-high {
		background-color: rgba(245, 158, 11, 0.1);
		color: var(--color-warning);
	}

	/* Status Badge */
	.status-badge {
		padding: var(--spacing-1) var(--spacing-2);
		border-radius: var(--radius-full);
		font-size: var(--font-size-xs);
		font-weight: var(--font-weight-medium);
		text-transform: capitalize;
		white-space: nowrap;
	}

	.status-pending {
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

	/* Notes */
	.task-notes {
		color: var(--color-text-secondary);
		font-size: var(--font-size-sm);
		line-height: var(--line-height-relaxed);
		margin: 0;
		display: -webkit-box;
		-webkit-line-clamp: 2;
		-webkit-box-orient: vertical;
		overflow: hidden;
	}

	/* Metadata */
	.task-metadata {
		display: flex;
		gap: var(--spacing-4);
		flex-wrap: wrap;
		padding-top: var(--spacing-2);
		border-top: 1px solid var(--color-border);
	}

	.metadata-item {
		display: flex;
		align-items: center;
		gap: var(--spacing-2);
	}

	.metadata-icon {
		width: 16px;
		height: 16px;
		color: var(--color-text-tertiary);
		flex-shrink: 0;
	}

	.metadata-text {
		font-size: var(--font-size-xs);
		color: var(--color-text-secondary);
	}

	/* Responsive */
	@media (max-width: 640px) {
		.task-metadata {
			flex-direction: column;
			align-items: flex-start;
			gap: var(--spacing-2);
		}
	}
</style>
