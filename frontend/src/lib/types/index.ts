export interface ApiKey {
	apiKey: string;
	userId: string;
	username: string;
	createdAt: string;
}

export interface Project {
	id: string;
	name: string;
	team: string;
	description: string;
	status: 'planning' | 'in_progress' | 'completed' | 'on_hold';
	createdAt: string;
	updatedAt: string;
	taskCount: number;
	completedTasks: number;
}

export interface Task {
	id: string;
	name: string;
	priority: 'low' | 'medium' | 'high';
	belongs_to: string;
	start_date: string | null;
	end_date: string | null;
	notes: string | null;
	effort: number | null;
	assigned_to: string[];
	status: 'pending' | 'in_progress' | 'completed';
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
