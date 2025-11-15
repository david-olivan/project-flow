export interface ApiKey {
	apiKey: string;
	userId: string;
	username: string;
	createdAt: string;
}

export interface Project {
	id: string;
	name: string;
	description: string;
	status: 'planning' | 'in_progress' | 'completed' | 'on_hold';
	createdAt: string;
	updatedAt: string;
	taskCount: number;
	completedTasks: number;
}

export interface User {
	userId: string;
	username: string;
}

export interface AuthState {
	isAuthenticated: boolean;
	apiKey: string | null;
	user: User | null;
}
