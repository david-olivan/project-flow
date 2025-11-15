<script lang="ts">
	/**
	 * Input Component - davidom Brand Kit
	 *
	 * Reusable input field component with validation display
	 */

	interface InputProps {
		value?: string;
		placeholder?: string;
		type?: 'text' | 'password' | 'email' | 'number';
		disabled?: boolean;
		error?: string;
		label?: string;
		id?: string;
		required?: boolean;
		oninput?: (event: Event) => void;
	}

	let {
		value = $bindable(''),
		placeholder = '',
		type = 'text',
		disabled = false,
		error = '',
		label = '',
		id = '',
		required = false,
		oninput
	}: InputProps = $props();

	// Generate a unique ID if not provided
	const inputId = id || `input-${Math.random().toString(36).substr(2, 9)}`;
</script>

<div class="input-wrapper">
	{#if label}
		<label for={inputId} class="input-label">
			{label}
			{#if required}
				<span class="required">*</span>
			{/if}
		</label>
	{/if}

	<input
		{type}
		{placeholder}
		{disabled}
		id={inputId}
		bind:value
		oninput={oninput}
		class="input"
		class:input-error={error}
		aria-invalid={!!error}
		aria-describedby={error ? `${inputId}-error` : undefined}
		{required}
	/>

	{#if error}
		<p class="error-message" id="{inputId}-error" role="alert">
			{error}
		</p>
	{/if}
</div>

<style>
	.input-wrapper {
		display: flex;
		flex-direction: column;
		gap: var(--spacing-2);
		width: 100%;
	}

	.input-label {
		font-size: var(--font-size-sm);
		font-weight: var(--font-weight-medium);
		color: var(--color-text-primary);
	}

	.required {
		color: var(--color-error);
	}

	.input {
		width: 100%;
		padding: var(--spacing-3) var(--spacing-4);

		font-family: var(--font-family-primary);
		font-size: var(--font-size-base);
		line-height: var(--line-height-normal);

		color: var(--color-text-primary);
		background-color: var(--color-surface);
		border: 2px solid var(--color-border);
		border-radius: var(--radius-input);

		transition: var(--transition-colors);
	}

	.input::placeholder {
		color: var(--color-text-tertiary);
	}

	.input:hover:not(:disabled) {
		border-color: var(--color-primary-300);
	}

	.input:focus {
		outline: none;
		border-color: var(--color-primary-500);
		box-shadow: 0 0 0 3px rgba(168, 85, 247, 0.1);
	}

	.input:disabled {
		opacity: 0.5;
		cursor: not-allowed;
		background-color: var(--color-neutral-100);
	}

	[data-theme='dark'] .input:disabled {
		background-color: var(--color-neutral-800);
	}

	.input-error {
		border-color: var(--color-error);
	}

	.input-error:focus {
		box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1);
	}

	.error-message {
		font-size: var(--font-size-sm);
		color: var(--color-error);
		margin: 0;
	}
</style>
