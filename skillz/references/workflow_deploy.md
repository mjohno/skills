# Skill Deploy Workflow

## Context
Synchronize a local skill directory to a `TARGET_DIRECTORY` for active use.

## Inputs
1. Source skill directory
2. Target directory (`TARGET_DIRECTORY`)
3. Sync method (symlink/junction or rsync/robocopy)

## Steps

### Phase 1: Preparation
1. **Identify Source**: Confirm the source skill directory.
2. **Identify Target**: Confirm the target directory.
3. **Choose Method**: Decide between **Real-time Syncing** (Symlinks/Junctions) or **Manual Mirroring** (Rsync/Robocopy).

### Phase 2: Confirmation
1. **Confirm Plan**: Explicitly state the source, target, and chosen method to the user.
2. **Command Generation**: Provide the exact command line for the user to execute.
   - *Example (Linux Symlink):* `ln -s "$(pwd)/skills" ${TARGET_DIRECTORY}`
   - *Example (Windows Junction):* `mklink /J "%USERPROFILE%\%TARGET_DIRECTORY%" "%CD%\skills"`
3. **User Approval**: Wait for explicit user acceptance before providing any deployment commands.

### Phase 3: Execution
1. **Run Command**: Execute the deployment plan.
2. **Verify Results**: Confirm that the files have been successfully synchronized to the target directory.

## Patterns
- **Symlink/Junction**: Real-time sync, bidirectional changes
- **Rsync/Robocopy**: One-way copy, no live sync

## Constraints
1. Requires explicit user approval before execution

## Outputs
Synchronized skill directory at target
