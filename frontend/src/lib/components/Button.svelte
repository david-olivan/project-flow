<script lang="ts">
	/**
	 * Button Component - davidom Brand Kit
	 *
	 * Reusable button component with variants and sizes
	 */

	type ButtonVariant = 'primary' | 'secondary' | 'tertiary';
	type ButtonSize = 'sm' | 'base' | 'lg';

	interface ButtonProps {
		variant?: ButtonVariant;
		size?: ButtonSize;
		disabled?: boolean;
		type?: 'button' | 'submit' | 'reset';
		onclick?: () => void;
	}

	let {
		variant = 'primary',
		size = 'base',
		disabled = false,
		type = 'button',
		onclick,
		children
	}: ButtonProps = $props();
</script>

<button
	{type}
	{disabled}
	class="button button-{variant} button-{size}"
	onclick={onclick}
	aria-disabled={disabled}
>
	{@render children?.()}
</button>

<style>
	.button {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		gap: var(--spacing-2);
		padding: var(--spacing-3) var(--spacing-6);

		font-family: var(--font-family-primary);
		font-size: var(--font-size-base);
		font-weight: var(--font-weight-medium);
		line-height: var(--line-height-normal);
		text-decoration: none;

		border: 2px solid transparent;
		border-radius: var(--radius-button);

		cursor: pointer;
		transition: var(--transition-all);
		user-select: none;
	}

	/* Primary Button (Filled) */
	.button-primary {
		color: var(--color-text-inverse);
		background-color: var(--color-primary-600);
		box-shadow: var(--shadow-sm);
	}

	.button-primary:hover:not(:disabled) {
		background-color: var(--color-primary-700);
		box-shadow: var(--shadow-md);
		transform: translateY(-1px);
	}

	.button-primary:active:not(:disabled) {
		transform: translateY(0);
		box-shadow: var(--shadow-sm);
	}

	.button-primary:focus-visible {
		outline: 2px solid var(--color-primary-500);
		outline-offset: 2px;
	}

	/* Secondary Button (Outlined) */
	.button-secondary {
		color: var(--color-primary-600);
		background-color: transparent;
		border-color: var(--color-primary-600);
	}

	.button-secondary:hover:not(:disabled) {
		color: var(--color-text-inverse);
		background-color: var(--color-primary-600);
		transform: translateY(-1px);
		box-shadow: var(--shadow-sm);
	}

	.button-secondary:active:not(:disabled) {
		transform: translateY(0);
	}

	.button-secondary:focus-visible {
		outline: 2px solid var(--color-primary-500);
		outline-offset: 2px;
	}

	/* Tertiary Button (Ghost) */
	.button-tertiary {
		color: var(--color-primary-600);
		background-color: transparent;
	}

	.button-tertiary:hover:not(:disabled) {
		background-color: var(--color-primary-50);
		color: var(--color-primary-700);
	}

	.button-tertiary:active:not(:disabled) {
		background-color: var(--color-primary-100);
	}

	.button-tertiary:focus-visible {
		outline: 2px solid var(--color-primary-500);
		outline-offset: 2px;
	}

	/* Dark mode adjustments for tertiary */
	[data-theme='dark'] .button-tertiary:hover:not(:disabled) {
		background-color: var(--color-primary-900);
		color: var(--color-primary-300);
	}

	[data-theme='dark'] .button-tertiary:active:not(:disabled) {
		background-color: var(--color-primary-800);
	}

	/* Button Sizes */
	.button-sm {
		padding: var(--spacing-2) var(--spacing-4);
		font-size: var(--font-size-sm);
	}

	.button-lg {
		padding: var(--spacing-4) var(--spacing-8);
		font-size: var(--font-size-lg);
	}

	/* Disabled State */
	.button:disabled {
		opacity: 0.5;
		cursor: not-allowed;
		pointer-events: none;
	}
</style>
