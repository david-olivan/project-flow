/**
 * Validation utilities for ProjectFlow
 */

/**
 * Validates API key format
 * Format: pFlow010-[22 chars]-[22 chars]-[22 chars]
 */
export function validateApiKeyFormat(apiKey: string): boolean {
	// API key pattern: pFlow010- followed by three segments of alphanumeric + underscore/hyphen
	const apiKeyPattern = /^pFlow010-[A-Za-z0-9_-]{22}-[A-Za-z0-9_-]{22}-[A-Za-z0-9_-]{22}$/;
	return apiKeyPattern.test(apiKey);
}

/**
 * Validates that a string is not empty
 */
export function isNotEmpty(value: string): boolean {
	return value.trim().length > 0;
}
