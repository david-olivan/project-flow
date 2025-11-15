/**
 * Authentication Store
 *
 * Manages authentication state using Svelte stores
 *
 * TODO (TECH DEBT): Security considerations
 * - Storing API keys in localStorage is not secure for production
 * - Should migrate to httpOnly cookies with JWT tokens
 * - Should implement token refresh mechanism
 * - Should add CSRF protection
 */

import { writable, derived } from 'svelte/store';
import type { AuthState, User } from '$lib/types';
import { validateApiKey, logout as logoutService } from '$lib/services/auth.service';
import { goto } from '$app/navigation';
import { browser } from '$app/environment';

// Initial state
const initialState: AuthState = {
	isAuthenticated: false,
	apiKey: null,
	user: null
};

// Create the auth store
function createAuthStore() {
	const { subscribe, set, update } = writable<AuthState>(initialState);

	return {
		subscribe,

		/**
		 * Initialize auth state from localStorage
		 */
		init: () => {
			if (!browser) return;

			const savedApiKey = localStorage.getItem('apiKey');
			const savedUser = localStorage.getItem('user');

			if (savedApiKey && savedUser) {
				set({
					isAuthenticated: true,
					apiKey: savedApiKey,
					user: JSON.parse(savedUser)
				});
			}
		},

		/**
		 * Attempt to login with an API key
		 * @param apiKey - The API key to validate
		 * @returns true if login successful, false otherwise
		 */
		login: async (apiKey: string): Promise<boolean> => {
			const user = await validateApiKey(apiKey);

			if (user) {
				// Store in localStorage
				if (browser) {
					localStorage.setItem('apiKey', apiKey);
					localStorage.setItem('user', JSON.stringify(user));
				}

				// Update store
				set({
					isAuthenticated: true,
					apiKey,
					user
				});

				return true;
			}

			return false;
		},

		/**
		 * Logout the current user
		 */
		logout: () => {
			logoutService();
			set(initialState);
			goto('/login');
		},

		/**
		 * Check if user is authenticated
		 */
		checkAuth: (): boolean => {
			if (!browser) return false;

			const savedApiKey = localStorage.getItem('apiKey');
			return !!savedApiKey;
		}
	};
}

// Export the store
export const authStore = createAuthStore();

// Derived stores for convenience
export const isAuthenticated = derived(authStore, ($auth) => $auth.isAuthenticated);
export const currentUser = derived(authStore, ($auth) => $auth.user);
