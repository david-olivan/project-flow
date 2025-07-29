# Task & Project Management Tool - PRD & Technical Specifications

## 1. Product Overview

### 1.1 Product Vision
A minimalistic, role-based task and project management tool with advanced time tracking capabilities, featuring dual board types and granular project-task associations.

### 1.2 Key Differentiators
- **Dual Board System**: Project boards (1:1 with projects) and Team boards (multi-project)
- **Advanced Time Tracking**: Granular vs Pomodoro tracking modes
- **Cross-Board Task Synchronization**: Tasks auto-populate between team and project boards
- **Comprehensive Time Analytics**: Project-level time breakdowns with multi-user aggregation

---

## 2. User Roles & Permissions

### 2.1 Role Hierarchy
```
Admin (Full Access)
├── Project Lead (Project Management)
├── Team Lead (Team Management)
└── Team Member (Task Execution)
```

### 2.2 Permission Matrix
| Feature | Admin | Project Lead | Team Lead | Team Member |
|---------|--------|--------------|-----------|-------------|
| Create/Delete Projects | ✅ | ✅ | ❌ | ❌ |
| Manage Project Boards | ✅ | ✅ (Own) | ❌ | ❌ |
| Manage Team Boards | ✅ | ❌ | ✅ (Own) | ❌ |
| Create/Edit Tasks | ✅ | ✅ | ✅ | ✅ (Assigned) |
| View Time Analytics | ✅ | ✅ (Projects) | ✅ (Teams) | ✅ (Own) |
| User Management | ✅ | ❌ | ❌ | ❌ |

---

## 3. Core Features

### 3.1 Board Management

#### 3.1.1 Project Boards
- **One-to-One Relationship**: Each project has exactly one board
- **Auto-Creation**: Created automatically when project is created
- **Task Association**: All tasks automatically linked to the project
- **Access Control**: Visible to project members and leads

#### 3.1.2 Team Boards
- **Multi-Project Support**: Can contain tasks from multiple projects
- **Task Categories**:
  - Project-associated tasks
  - Operational tasks (daily operations)
  - Service tasks (punctual, non-project work)
- **Cross-Population**: Project-associated tasks sync to project boards

### 3.2 Task Management

#### 3.2.1 Task Properties
```json
{
  "id": "uuid",
  "title": "string",
  "description": "text",
  "status": "todo|in-progress|review|done",
  "priority": "low|medium|high|urgent",
  "assignee": "user_id",
  "project_id": "uuid|null",
  "category": "project|operational|service",
  "estimated_time": "minutes",
  "actual_time": "minutes",
  "created_at": "datetime",
  "due_date": "datetime|null",
  "tags": ["string"]
}
```

#### 3.2.2 Drag & Drop Functionality
- **Status Transitions**: Drag tasks between columns (Todo, In Progress, Review, Done)
- **Priority Reordering**: Vertical drag within columns
- **Cross-Board Movement**: Tasks can move between team and project boards
- **Real-time Updates**: Live synchronization across all connected users

### 3.3 Time Tracking System

#### 3.3.1 Tracking Modes
1. **Granular Tracking**
   - Continuous time tracking
   - Start/stop timers
   - Manual time entry
   - Break tracking

2. **Pomodoro Tracking**
   - 25-minute focused sessions
   - 5-minute short breaks
   - 15-minute long breaks (every 4 pomodoros)
   - Session completion tracking

#### 3.3.2 Timer Features
- **Active Timer**: Global timer accessible from anywhere
- **Task Selection**: Choose current task when starting timer
- **Automatic Logging**: Time automatically added to task and project totals
- **Pause/Resume**: Support for interruptions
- **Background Tracking**: Timer continues across page navigation

### 3.4 Analytics & Reporting

#### 3.4.1 Project Analytics
- **Time Breakdown**: Total estimated vs actual time
- **Task Progress**: Completion rates and velocity
- **Member Contributions**: Individual time contributions
- **Timeline View**: Project timeline with milestones

#### 3.4.2 Individual Analytics
- **Personal Dashboard**: Own time tracking and productivity metrics
- **Task History**: Completed tasks with time logs
- **Productivity Trends**: Daily/weekly/monthly patterns

---

## 4. Technical Architecture

### 4.1 Backend Stack
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT with refresh tokens
- **Real-time**: WebSockets for live updates
- **Caching**: Redis for session management and real-time data
- **File Storage**: AWS S3 or local storage for attachments

### 4.2 Frontend Options

#### Recommended: **SvelteKit**
**Why SvelteKit**:
- Excellent performance for drag & drop interfaces
- Built-in SSR and routing
- Smaller bundle size than React
- Great TypeScript support
- Growing ecosystem

**Alternative Options**:
- **Astro + React**: Use Astro for static pages, React islands for interactive components
- **Next.js**: If you want to deepen React skills
- **Nuxt 3**: If interested in Vue ecosystem

### 4.3 Database Schema

#### 4.3.1 Core Tables
```sql
-- Users and Authentication
users (id, email, username, password_hash, role, created_at, updated_at)
user_sessions (id, user_id, token_hash, expires_at)

-- Projects and Teams
projects (id, name, description, status, created_by, created_at, updated_at)
teams (id, name, description, team_lead_id, created_at, updated_at)
project_members (project_id, user_id, role, joined_at)
team_members (team_id, user_id, joined_at)

-- Boards
boards (id, name, type, project_id, team_id, tracking_mode, created_at)
board_columns (id, board_id, name, position, status_type)

-- Tasks
tasks (id, title, description, status, priority, assignee_id, project_id, 
       category, estimated_minutes, actual_minutes, board_id, column_id, 
       position, created_at, updated_at, due_date)

-- Time Tracking
time_entries (id, task_id, user_id, start_time, end_time, duration_minutes, 
              tracking_mode, session_type, created_at)
pomodoro_sessions (id, user_id, task_id, completed_intervals, break_time, 
                   created_at, completed_at)
```

### 4.4 API Design

#### 4.4.1 Core Endpoints
```
Authentication:
POST /auth/login
POST /auth/refresh
POST /auth/logout

Projects:
GET /projects
POST /projects
GET /projects/{id}
PUT /projects/{id}
DELETE /projects/{id}
GET /projects/{id}/analytics

Boards:
GET /boards
POST /boards
GET /boards/{id}
PUT /boards/{id}
DELETE /boards/{id}

Tasks:
GET /tasks
POST /tasks
GET /tasks/{id}
PUT /tasks/{id}
DELETE /tasks/{id}
PUT /tasks/{id}/move

Time Tracking:
POST /time/start
POST /time/stop
POST /time/entry
GET /time/analytics
POST /pomodoro/start
POST /pomodoro/complete
```

#### 4.4.2 WebSocket Events
```
task.created
task.updated
task.moved
timer.started
timer.stopped
board.updated
user.joined
user.left
```

---

## 5. User Experience (UX) Requirements

### 5.1 Dashboard Layout
```
┌─ Header (Logo, Timer, User Menu) ─────────────────────┐
├─ Sidebar ─┬─ Main Content Area ─────────────────────┤
│           │                                         │
│ - Projects│  ┌─ Board View ─────────────────────┐   │
│ - Teams   │  │                                 │   │
│ - My Tasks│  │ [Todo] [In Progress] [Done]     │   │
│ - Analytics│  │   │        │          │        │   │
│           │  │ [Task]   [Task]    [Task]       │   │
│           │  │ [Task]   [Task]    [Task]       │   │
│           │  │                                 │   │
│           │  └─────────────────────────────────┘   │
└───────────┴─────────────────────────────────────────┘
```

### 5.2 Key Interactions
- **Quick Task Creation**: Floating action button or keyboard shortcut
- **Inline Editing**: Click to edit task titles and descriptions
- **Timer Integration**: Start timer from any task card
- **Search & Filter**: Global search with project/assignee filters
- **Keyboard Shortcuts**: Common actions accessible via keyboard

### 5.3 Mobile Responsiveness
- **Mobile-First Design**: Touch-friendly drag & drop
- **Progressive Web App**: Offline capability for viewing tasks
- **Responsive Breakpoints**: 
  - Mobile: < 768px (single column)
  - Tablet: 768px - 1024px (two columns)
  - Desktop: > 1024px (full board view)

---

## 6. Development Phases

### Phase 1: Core Foundation (Weeks 1-3)
- [ ] User authentication and authorization
- [ ] Basic project and team management
- [ ] Simple task CRUD operations
- [ ] Basic board layout (no drag & drop yet)

### Phase 2: Board Functionality (Weeks 4-6)
- [ ] Drag & drop implementation
- [ ] Real-time updates via WebSockets
- [ ] Task status management
- [ ] Cross-board task synchronization

### Phase 3: Time Tracking (Weeks 7-9)
- [ ] Timer implementation
- [ ] Granular time tracking
- [ ] Pomodoro mode
- [ ] Basic time analytics

### Phase 4: Analytics & Polish (Weeks 10-12)
- [ ] Advanced analytics dashboard
- [ ] Project time breakdowns
- [ ] Performance optimization
- [ ] UI/UX refinements

---

## 7. Technical Considerations

### 7.1 Performance Requirements
- **Page Load Time**: < 2 seconds initial load
- **Drag & Drop Latency**: < 50ms response time
- **Real-time Updates**: < 100ms propagation
- **Database Queries**: < 200ms for complex analytics

### 7.2 Security Requirements
- **Authentication**: JWT with secure HTTP-only cookies
- **Authorization**: Role-based access control on all endpoints
- **Data Validation**: Input sanitization and validation
- **Rate Limiting**: API rate limiting to prevent abuse

### 7.3 Scalability Considerations
- **Database Indexing**: Proper indexes on frequently queried fields
- **Caching Strategy**: Redis for real-time data and session management
- **File Storage**: External storage for attachments
- **Background Jobs**: Celery for time-intensive operations

---

## 8. Success Metrics

### 8.1 User Engagement
- Daily active users
- Task completion rate
- Time tracking adoption rate
- Session duration

### 8.2 Performance Metrics
- Page load times
- API response times
- WebSocket connection stability
- Database query performance

### 8.3 Business Metrics
- User retention rate
- Feature adoption rate
- Time saved vs traditional tools
- User satisfaction scores

---

## 9. Future Enhancements

### 9.1 Short Term (3-6 months)
- [ ] File attachments for tasks
- [ ] Task comments and mentions
- [ ] Email notifications
- [ ] Export functionality (CSV, PDF)

### 9.2 Long Term (6-12 months)
- [ ] Mobile applications (React Native/Flutter)
- [ ] Advanced automation and workflows
- [ ] Integration with external tools (Slack, GitHub)
- [ ] Custom board templates
- [ ] Advanced reporting and insights

---

This comprehensive PRD and technical specification provides a solid foundation for building your task management tool. The modular approach allows you to build incrementally while maintaining a clear vision of the final product.