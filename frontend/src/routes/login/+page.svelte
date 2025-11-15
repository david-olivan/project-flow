<script lang="ts">
	/**
	 * Login Page - API Key Authentication
	 *
	 * TODO (TECH DEBT): Replace API key authentication with username/password
	 * This is temporary for initial development. Future implementation should:
	 * 1. Add user registration with email/password
	 * 2. Implement JWT-based authentication
	 * 3. Add refresh token mechanism
	 * 4. Move API key to user settings for API access only
	 */

	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { authStore } from '$lib/stores/auth';
	import Button from '$lib/components/Button.svelte';
	import Input from '$lib/components/Input.svelte';
	import Logo from '$lib/components/Logo.svelte';

	let apiKey = $state('');
	let error = $state('');
	let isLoading = $state(false);

	// Redirect if already authenticated
	onMount(() => {
		authStore.init();
		if ($authStore.isAuthenticated) {
			goto('/dashboard');
		}
	});

	async function handleSubmit(event: Event) {
		event.preventDefault();
		error = '';

		if (!apiKey.trim()) {
			error = 'Please enter your API key';
			return;
		}

		isLoading = true;

		try {
			const success = await authStore.login(apiKey);

			if (success) {
				goto('/dashboard');
			} else {
				error = 'Invalid API key. Please check your key and try again.';
			}
		} catch (err) {
			error = 'An error occurred. Please try again.';
			console.error('Login error:', err);
		} finally {
			isLoading = false;
		}
	}

	// Subscribe to auth store
	let authState = $derived($authStore);
</script>

<svelte:head>
	<title>Login - ProjectFlow</title>
</svelte:head>

<div class="login-page">
	<div class="login-container">
		<div class="login-card">
			<!-- Logo and Header -->
			<div class="login-header">
				<Logo size="lg" />
				<h1 class="login-title">Welcome Back</h1>
				<p class="login-subtitle">Enter your API key to continue</p>
			</div>

			<!-- Login Form -->
			<form class="login-form" onsubmit={handleSubmit}>
				<Input
					bind:value={apiKey}
					type="text"
					label="API Key"
					placeholder="pFlow010-xxxxxxxx-xxxxxxxx-xxxxxxxx"
					error={error}
					disabled={isLoading}
					required
				/>

				<Button type="submit" variant="primary" size="lg" disabled={isLoading}>
					{isLoading ? 'Signing in...' : 'Sign In'}
				</Button>
			</form>

			<!-- Help Text -->
			<div class="login-footer">
				<p class="help-text">
					Don't have an API key? Contact your administrator or check your account settings.
				</p>
			</div>
		</div>

		<!-- Development Note -->
		<div class="dev-note">
			<p>
				<strong>Dev Note:</strong> Using API key authentication temporarily. Will be replaced with username/password
				in future versions.
			</p>
			<details>
				<summary>Test API Keys</summary>
				<ul>
					<li><code>pFlow010-3JHYLBtEWNL_kAZ8T5XDcuc2QOFNJD0-H9v1w-90bxk</code> (davidom)</li>
					<li><code>pFlow010-7KNXMCuFXOM_lBA9U6YEdvd3RPGOKD1-I0w2x-01cyl</code> (demo_user)</li>
					<li><code>pFlow010-9MPZOEwHZPO_nDC0W8ZGfxf5TRHQMF3-K2y4z-23ezn</code> (test_user)</li>
				</ul>
			</details>
		</div>
	</div>
</div>

<style>
	.login-page {
		min-height: 100vh;
		display: flex;
		align-items: center;
		justify-content: center;
		padding: var(--spacing-4);
		background: linear-gradient(
			135deg,
			var(--color-primary-50) 0%,
			var(--color-accent-50) 100%
		);
	}

	[data-theme='dark'] .login-page {
		background: linear-gradient(135deg, var(--color-primary-900) 0%, var(--color-accent-900) 100%);
	}

	.login-container {
		width: 100%;
		max-width: 480px;
		display: flex;
		flex-direction: column;
		gap: var(--spacing-6);
	}

	.login-card {
		background-color: var(--color-surface-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-2xl);
		padding: var(--spacing-10);
		box-shadow: var(--shadow-2xl);
	}

	.login-header {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: var(--spacing-4);
		text-align: center;
		margin-bottom: var(--spacing-8);
	}

	.login-title {
		font-size: var(--font-size-3xl);
		font-weight: var(--font-weight-bold);
		color: var(--color-text-primary);
		margin: 0;
	}

	.login-subtitle {
		font-size: var(--font-size-base);
		color: var(--color-text-secondary);
		margin: 0;
	}

	.login-form {
		display: flex;
		flex-direction: column;
		gap: var(--spacing-6);
	}

	.login-footer {
		margin-top: var(--spacing-6);
		padding-top: var(--spacing-6);
		border-top: 1px solid var(--color-border);
		text-align: center;
	}

	.help-text {
		font-size: var(--font-size-sm);
		color: var(--color-text-tertiary);
		margin: 0;
	}

	/* Development Note Styling */
	.dev-note {
		background-color: var(--color-warning);
		color: var(--color-neutral-900);
		padding: var(--spacing-4);
		border-radius: var(--radius-lg);
		font-size: var(--font-size-sm);
	}

	.dev-note strong {
		font-weight: var(--font-weight-bold);
	}

	.dev-note details {
		margin-top: var(--spacing-3);
	}

	.dev-note summary {
		cursor: pointer;
		font-weight: var(--font-weight-medium);
		margin-bottom: var(--spacing-2);
	}

	.dev-note ul {
		list-style: none;
		padding: 0;
		margin: 0;
		display: flex;
		flex-direction: column;
		gap: var(--spacing-2);
	}

	.dev-note code {
		background-color: rgba(0, 0, 0, 0.1);
		padding: var(--spacing-1) var(--spacing-2);
		border-radius: var(--radius-sm);
		font-family: var(--font-family-mono);
		font-size: var(--font-size-xs);
		word-break: break-all;
		display: inline-block;
	}

	/* Responsive */
	@media (max-width: 640px) {
		.login-card {
			padding: var(--spacing-6);
		}

		.login-title {
			font-size: var(--font-size-2xl);
		}

		.dev-note {
			font-size: var(--font-size-xs);
		}
	}
</style>
