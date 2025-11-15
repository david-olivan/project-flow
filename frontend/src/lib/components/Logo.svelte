<script lang="ts">
	/**
	 * Logo Component - ProjectFlow Branding
	 *
	 * Displays the ProjectFlow logo/title with brand styling
	 */

	interface LogoProps {
		size?: 'sm' | 'md' | 'lg';
		showIcon?: boolean;
		showText?: boolean;
	}

	let { size = 'md', showIcon = true, showText = true }: LogoProps = $props();
</script>

<div class="logo logo-{size}">
	{#if showIcon}
		<div class="logo-icon">
			<svg
				width="100%"
				height="100%"
				viewBox="0 0 40 40"
				fill="none"
				xmlns="http://www.w3.org/2000/svg"
			>
				<!-- Simple geometric icon representing flow/project management -->
				<rect x="4" y="4" width="12" height="12" rx="2" class="icon-primary" />
				<rect x="4" y="20" width="12" height="12" rx="2" class="icon-accent" />
				<rect x="20" y="12" width="16" height="16" rx="2" class="icon-primary" />
				<path d="M10 16 L20 20" class="icon-line" stroke-width="2" stroke-linecap="round" />
				<path d="M10 26 L20 26" class="icon-line" stroke-width="2" stroke-linecap="round" />
			</svg>
		</div>
	{/if}
	{#if showText}
		<span class="logo-text">ProjectFlow</span>
	{/if}
</div>

<style>
	.logo {
		display: flex;
		align-items: center;
		gap: var(--spacing-3);
	}

	.logo-icon {
		display: flex;
		align-items: center;
		justify-content: center;
		flex-shrink: 0;
	}

	.icon-primary {
		fill: var(--color-primary-600);
	}

	.icon-accent {
		fill: var(--color-accent-500);
	}

	.icon-line {
		stroke: var(--color-primary-400);
	}

	.logo-text {
		font-family: var(--font-family-heading);
		font-weight: var(--font-weight-bold);
		color: var(--color-text-primary);
		letter-spacing: var(--letter-spacing-tight);
	}

	/* Size Variations */
	.logo-sm .logo-icon {
		width: 24px;
		height: 24px;
		min-width: 24px;
		min-height: 24px;
	}

	.logo-sm .logo-text {
		font-size: var(--font-size-lg);
	}

	.logo-md .logo-icon {
		width: 32px;
		height: 32px;
		min-width: 32px;
		min-height: 32px;
	}

	.logo-md .logo-text {
		font-size: var(--font-size-2xl);
	}

	.logo-lg .logo-icon {
		width: 48px;
		height: 48px;
		min-width: 48px;
		min-height: 48px;
	}

	.logo-lg .logo-text {
		font-size: var(--font-size-4xl);
	}
</style>
