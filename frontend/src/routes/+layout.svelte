<script lang="ts">
	import { onMount } from 'svelte';
	import '../styles/variables.css';
	import '../styles/reset.css';
	import '../styles/global.css';

	let { children } = $props();

	// Initialize theme on mount
	onMount(() => {
		// Check for saved theme preference or default to system preference
		const savedTheme = localStorage.getItem('theme');
		const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
		const theme = savedTheme || (prefersDark ? 'dark' : 'light');

		document.documentElement.setAttribute('data-theme', theme);
	});
</script>

{@render children()}
