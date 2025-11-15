/**
 * Authentication Service
 *
 * TODO (TECH DEBT): Replace API key authentication with username/password
 * This is temporary for initial development. Future implementation should:
 * 1. Add user registration with email/password
 * 2. Implement JWT-based authentication
 * 3. Add refresh token mechanism
 * 4. Move API key to user settings for API access only
 */

import type { ApiKey, User } from '$lib/types';
import { validateApiKeyFormat } from '$lib/utils/validators';

/**
 * Validates an API key against the mock backend
 * @param apiKey - The API key to validate
 * @returns User object if valid, null otherwise
 */
export async function validateApiKey(apiKey: string): Promise<User | null> {
	// First validate format
	if (!validateApiKeyFormat(apiKey)) {
		return null;
	}

	// TODO (TECH DEBT): Replace with actual API call
	// const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/api/auth/validate`, {
	//   method: 'POST',
	//   headers: { 'Content-Type': 'application/json' },
	//   body: JSON.stringify({ apiKey })
	// });

	// Simulate async API call with mock data from static folder
	await new Promise((resolve) => setTimeout(resolve, 300));

	// Fetch mock data from static folder
	const response = await fetch('/mock_data/api_keys.json');
	const apiKeysData = await response.json();

	// Find matching API key in mock data
	const validKey = apiKeysData.validKeys.find((key: ApiKey) => key.apiKey === apiKey);

	if (validKey) {
		return {
			userId: validKey.userId,
			username: validKey.username
		};
	}

	return null;
}

/**
 * Logs out the user by clearing auth data
 */
export function logout(): void {
	// TODO (TECH DEBT): When switching to JWT, also invalidate the token on the server
	localStorage.removeItem('apiKey');
	localStorage.removeItem('user');
}
