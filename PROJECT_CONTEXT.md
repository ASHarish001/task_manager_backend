# Smart Task Manager - Project Context

## Overview

Smart Task Manager is a full-stack learning project for building practical experience with modern web development.

The current focus is Phase 1: a personal task management system. Team collaboration features belong to Phase 2 and should not be implemented yet.

## Phase 1 Scope

Authenticated users can:

- Register and log in
- Create tasks
- View tasks
- Update tasks
- Delete tasks
- Search tasks
- Filter tasks
- View dashboard statistics

Important rule: users must only access, modify, update, or delete their own tasks.

## Future Phase 2 Scope

Planned team features:

- Projects or workspaces
- Teams
- Role-based access control
- Task assignment
- Comments
- Notifications
- Team dashboards
- Activity tracking

Do not implement these during Phase 1.

## Tech Stack

Frontend:

- React
- TypeScript
- Material UI
- Axios
- React Router

Backend:

- Django
- Django REST Framework
- JWT authentication
- MySQL

## Backend Apps

### accounts

Responsibilities:

- User registration
- User login
- JWT authentication
- User profile management

### tasks

Responsibilities:

- Task CRUD operations
- Search and filtering
- Task status management
- Task priority management
- Dashboard statistics

### core

Responsibilities:

- Shared utilities
- Base models
- Common permissions
- Reusable helpers

## Authentication

Use JWT authentication.

Expected auth endpoints:

- Register
- Login
- Refresh token

Protected APIs require a JWT access token.

## Data Model

### User

Fields:

- id
- username
- email
- password
- created_at
- updated_at

### Task

Fields:

- id
- title
- description
- status
- priority
- due_date
- created_at
- updated_at
- owner, as a foreign key to User

Task status values:

- PENDING
- IN_PROGRESS
- COMPLETED

Task priority values:

- LOW
- MEDIUM
- HIGH

## API Principles

- Use RESTful APIs
- Return proper HTTP status codes
- Validate input with DRF serializers
- Protect private endpoints with JWT
- Enforce user-specific data isolation
- Use pagination for list endpoints

## Backend Coding Standards

- Follow Django best practices
- Use DRF generic views or viewsets where appropriate
- Keep business logic in services when complexity grows
- Use serializers for validation
- Use meaningful model methods
- Keep code clean and readable

## Frontend Coding Standards

- Use functional React components
- Use TypeScript interfaces
- Use Material UI components
- Maintain a clean folder structure
- Create reusable components where useful

## Current Roadmap

1. Project setup
   - Create Django project
   - Configure MySQL
   - Configure DRF
   - Configure JWT authentication

2. Accounts app
   - Registration API
   - Login API
   - Profile API

3. Tasks app
   - Task model
   - Task serializer
   - Task CRUD APIs
   - User-specific permissions

4. Dashboard APIs
   - Total tasks
   - Completed tasks
   - Pending tasks
   - Overdue tasks

5. Search and filtering
   - Search by title
   - Search by description
   - Filter by status
   - Filter by priority
   - Filter by due date

## Codex Notes

When continuing this project, first inspect the current Django files and compare them against this roadmap. Keep work scoped to Phase 1 unless the user explicitly asks to start Phase 2.
