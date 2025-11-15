/**
 * Sidebar State Store
 *
 * Manages sidebar collapse/expand state
 */

import { writable } from 'svelte/store';
import { browser } from '$app/environment';

interface SidebarState {
	isCollapsed: boolean;
	isAutoExpand: boolean; // Whether to expand on hover when collapsed
}

const initialState: SidebarState = {
	isCollapsed: false,
	isAutoExpand: true
};

function createSidebarStore() {
	const { subscribe, set, update } = writable<SidebarState>(initialState);

	return {
		subscribe,

		/**
		 * Initialize sidebar state from localStorage
		 */
		init: () => {
			if (!browser) return;

			const savedCollapsed = localStorage.getItem('sidebarCollapsed');
			const savedAutoExpand = localStorage.getItem('sidebarAutoExpand');

			if (savedCollapsed !== null || savedAutoExpand !== null) {
				set({
					isCollapsed: savedCollapsed === 'true',
					isAutoExpand: savedAutoExpand !== 'false' // Default to true
				});
			}
		},

		/**
		 * Toggle collapsed state
		 */
		toggleCollapsed: () => {
			update((state) => {
				const newCollapsed = !state.isCollapsed;
				if (browser) {
					localStorage.setItem('sidebarCollapsed', String(newCollapsed));
				}
				return { ...state, isCollapsed: newCollapsed };
			});
		},

		/**
		 * Toggle auto-expand on hover
		 */
		toggleAutoExpand: () => {
			update((state) => {
				const newAutoExpand = !state.isAutoExpand;
				if (browser) {
					localStorage.setItem('sidebarAutoExpand', String(newAutoExpand));
				}
				return { ...state, isAutoExpand: newAutoExpand };
			});
		},

		/**
		 * Set collapsed state directly
		 */
		setCollapsed: (collapsed: boolean) => {
			update((state) => {
				if (browser) {
					localStorage.setItem('sidebarCollapsed', String(collapsed));
				}
				return { ...state, isCollapsed: collapsed };
			});
		}
	};
}

export const sidebarStore = createSidebarStore();
