/**
 * View Preferences Store
 *
 * Manages user view preferences (grid/list mode) with localStorage persistence
 */

import { writable } from 'svelte/store';

type ViewMode = 'grid' | 'list';

interface ViewPreferences {
	projectViewMode: ViewMode;
}

const STORAGE_KEY = 'viewPreferences';

const defaultPreferences: ViewPreferences = {
	projectViewMode: 'grid'
};

function createViewPreferencesStore() {
	const { subscribe, set, update } = writable<ViewPreferences>(defaultPreferences);

	return {
		subscribe,
		init: () => {
			if (typeof window === 'undefined') return;

			const stored = localStorage.getItem(STORAGE_KEY);
			if (stored) {
				try {
					const preferences = JSON.parse(stored) as ViewPreferences;
					set(preferences);
				} catch (error) {
					console.error('Failed to parse view preferences from localStorage:', error);
					set(defaultPreferences);
				}
			} else {
				set(defaultPreferences);
			}
		},
		setProjectViewMode: (mode: ViewMode) => {
			update((prefs) => {
				const updated = { ...prefs, projectViewMode: mode };
				if (typeof window !== 'undefined') {
					localStorage.setItem(STORAGE_KEY, JSON.stringify(updated));
				}
				return updated;
			});
		},
		toggleProjectViewMode: () => {
			update((prefs) => {
				const mode = prefs.projectViewMode === 'grid' ? 'list' : 'grid';
				const updated = { ...prefs, projectViewMode: mode };
				if (typeof window !== 'undefined') {
					localStorage.setItem(STORAGE_KEY, JSON.stringify(updated));
				}
				return updated;
			});
		}
	};
}

export const viewPreferencesStore = createViewPreferencesStore();
export type { ViewMode };
