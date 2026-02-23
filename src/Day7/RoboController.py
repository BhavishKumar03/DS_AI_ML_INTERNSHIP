import random
import time


class Robot:
    def __init__(self, name, target_distance):
        self.name = name
        self.target_distance = target_distance
        self.current_position = 0
        self.current_direction = "FORWARD"
        self.speed = 0
        self.distance_travelled = 0
        self.checkpoints = []  # List to store checkpoints
        self.obstacle_list = []  # List to track obstacles encountered
        self.direction_history = []
        self.movement_log = []
        self.obstacle_status = "NONE"
        self.obstacles_encountered = []
        
    def add_checkpoint(self, checkpoint_name):
        """Add a new checkpoint to the journey"""
        checkpoint = {
            'id': len(self.checkpoints) + 1,
            'name': checkpoint_name,
            'position': self.current_position,
            'direction': self.current_direction,
            'time_reached': time.time()
        }
        self.checkpoints.append(checkpoint)
        print(f"✅ CHECKPOINT ADDED: {checkpoint_name} at position {self.current_position}m | ID: {checkpoint['id']}")
        return checkpoint
    
    def remove_checkpoint(self, checkpoint_id):
        """Remove a checkpoint by ID from the list"""
        for i, checkpoint in enumerate(self.checkpoints):
            if checkpoint['id'] == checkpoint_id:
                removed = self.checkpoints.pop(i)
                print(f"❌ CHECKPOINT REMOVED: {removed['name']} (ID: {checkpoint_id})")
                # Update IDs for remaining checkpoints
                for j, cp in enumerate(self.checkpoints):
                    cp['id'] = j + 1
                return True
        print(f"⚠️  Checkpoint with ID {checkpoint_id} not found!")
        return False
    
    def view_checkpoints(self):
        """Display all checkpoints in the list"""
        if not self.checkpoints:
            print("📍 No checkpoints added yet!")
            return
        
        print(f"\n{'='*50}")
        print(f"📋 CHECKPOINTS LIST ({len(self.checkpoints)} total)")
        print(f"{'='*50}")
        for checkpoint in self.checkpoints:
            print(f"[ID: {checkpoint['id']}] {checkpoint['name']}")
            print(f"    Position: {checkpoint['position']}m | Direction: {checkpoint['direction']}")
        print(f"{'='*50}\n")
    
    def update_checkpoint_name(self, checkpoint_id, new_name):
        """Update checkpoint name"""
        for checkpoint in self.checkpoints:
            if checkpoint['id'] == checkpoint_id:
                old_name = checkpoint['name']
                checkpoint['name'] = new_name
                print(f"✏️  CHECKPOINT RENAMED: {old_name} → {new_name}")
                return True
        print(f"⚠️  Checkpoint with ID {checkpoint_id} not found!")
        return False
    
    def add_obstacle_record(self, obstacle_type):
        """Record obstacle encountered"""
        obstacle_record = {
            'type': obstacle_type,
            'position': self.current_position,
            'time': time.time()
        }
        self.obstacles_encountered.append(obstacle_record)
        
    def determine_speed(self, obstacle_type):
        """Determine speed based on obstacle type"""
        self.obstacle_status = obstacle_type.upper()
        if obstacle_type.lower() == "none":
            self.speed = random.randint(40, 60)  # Normal speed (km/h)
            return "NORMAL"
        elif obstacle_type.lower() == "human":
            self.speed = 10  # Slow speed when human detected
            self.add_obstacle_record("HUMAN")
            return "SLOW"
        elif obstacle_type.lower() == "wall":
            self.speed = 0  # Stop when wall detected
            self.add_obstacle_record("WALL")
            return "STOPPED"
        else:
            self.speed = 25  # Default cautious speed
            return "CAUTIOUS"
    
    def handle_obstacle(self, obstacle_type):
        """Handle different types of obstacles"""
        if obstacle_type.lower() == "human":
            print(f"\n⚠️  HUMAN DETECTED! {self.name} is pausing...")
            self.movement_log.append("PAUSED (Human detected)")
            time.sleep(2)  # Pause for 2 seconds
            print(f"✓ {self.name} resuming movement...")
            self.movement_log.append("RESUMED after human detection")
            return True
        
        elif obstacle_type.lower() == "wall":
            print(f"\n🚧 WALL DETECTED! {self.name} changing direction...")
            self.movement_log.append("DIRECTION CHANGED (Wall detected)")
            return self.change_direction()
        
        else:
            print(f"\n✓ No obstacles ahead. {self.name} proceeding...")
            self.movement_log.append("No obstacles - proceeding normally")
            return True
    
    def change_direction(self):
        """Change direction when obstacle encountered"""
        directions = ["LEFT", "RIGHT", "BACK"]
        self.current_direction = random.choice(directions)
        print(f"📍 New direction: {self.current_direction}")
        return True
    
    def unexpected_change(self):
        """Random unexpected direction changes (simulating errors/adjustments)"""
        if random.random() < 0.2:  # 20% chance
            old_direction = self.current_direction
            directions = ["LEFT", "RIGHT", "BACK", "FORWARD"]
            self.current_direction = random.choice(directions)
            print(f"⚡ UNEXPECTED CHANGE! Direction changed from {old_direction} to {self.current_direction}")
            self.movement_log.append(f"Unexpected direction change: {old_direction} → {self.current_direction}")
            return True
        return False
    
    def check_50m_signal(self, remaining_distance):
        """Send signal before 50m to destination"""
        if remaining_distance <= 50 and remaining_distance > 40:
            print(f"\n🔔 SIGNAL: Approaching destination! Travelling {self.current_direction}")
            print(f"📍 Remaining distance: {remaining_distance} meters")
            self.movement_log.append(f"50M SIGNAL - Direction: {self.current_direction}, Remaining: {remaining_distance}m")
            return True
        return False
    
    def interactive_checkpoint_management(self):
        """Allow user to manage checkpoints during journey"""
        print(f"\n{'='*50}")
        print("📍 CHECKPOINT MANAGEMENT MENU")
        print(f"{'='*50}")
        print("1. Add new checkpoint")
        print("2. View all checkpoints")
        print("3. Remove checkpoint by ID")
        print("4. Update checkpoint name")
        print("5. Continue journey")
        print(f"{'='*50}")
        
        try:
            choice = input("Select option (1-5): ").strip()
        except EOFError:
            return True
        
        if choice == "1":
            try:
                cp_name = input("Enter checkpoint name: ").strip()
                if cp_name:
                    self.add_checkpoint(cp_name)
                else:
                    print("❌ Checkpoint name cannot be empty!")
            except EOFError:
                pass
        
        elif choice == "2":
            self.view_checkpoints()
        
        elif choice == "3":
            try:
                cp_id = int(input("Enter checkpoint ID to remove: ").strip())
                self.remove_checkpoint(cp_id)
            except (ValueError, EOFError):
                print("❌ Invalid ID!")
        
        elif choice == "4":
            try:
                cp_id = int(input("Enter checkpoint ID to update: ").strip())
                new_name = input("Enter new checkpoint name: ").strip()
                if new_name:
                    self.update_checkpoint_name(cp_id, new_name)
                else:
                    print("❌ Checkpoint name cannot be empty!")
            except (ValueError, EOFError):
                print("❌ Invalid ID!")
        
        elif choice == "5":
            print("✓ Continuing journey...")
            return True
        else:
            print("❌ Invalid option!")
        
        return False
    
    def detect_obstacle_ahead(self, scan_distance=50):
        """Detect if there's an obstacle within scan_distance meters ahead"""
        obstacles = ['none', 'human', 'wall']
        obstacle_ahead = random.choice(obstacles)
        distance_to_obstacle = random.randint(10, scan_distance)
        
        if obstacle_ahead in ['human', 'wall']:
            print(f"\n🔍 SENSOR ALERT: {obstacle_ahead.upper()} detected {distance_to_obstacle}m ahead!")
            return obstacle_ahead, distance_to_obstacle
        
        return 'none', None
    
    def simulate_movement(self):
        """Main movement simulation logic"""
        print(f"\n{'='*60}")
        print(f"🤖 {self.name.upper()} - STARTING JOURNEY")
        print(f"{'='*60}")
        print(f"Target Distance: {self.target_distance} meters")
        print(f"Starting Position: {self.current_position}m")
        print(f"Sensor Scanning Range: 50 meters ahead")
        print(f"\n")
        
        checkpoint_created = False
        movement_step = 0
        
        # Simulate movement
        while self.current_position < self.target_distance:
            movement_step += 1
            
            # Detect obstacles ahead using sensor (50 meters scan)
            obstacle_input, distance_to_obstacle = self.detect_obstacle_ahead(scan_distance=50)
            
            if obstacle_input != 'none':
                print(f"[Step {movement_step}] Obstacle ahead detected at {distance_to_obstacle}m!")
            else:
                print(f"\n[Step {movement_step}] Path clear - no obstacles detected")
            
            # Determine speed and movement strategy based on obstacle
            speed_status = self.determine_speed(obstacle_input)
            print(f"📊 Speed Status: {speed_status} ({self.speed} km/h)")
            
            # Handle obstacles
            if not self.handle_obstacle(obstacle_input):
                print("⚠️  Unable to proceed!")
                return False
            
            # Make decision for next movement
            remaining_distance = self.target_distance - self.current_position
            
            # Nested IF conditions for decision making based on speed status
            if speed_status == "NORMAL":
                if remaining_distance > 200:
                    move_distance = 50
                    action = "MOVING FORWARD (Full Speed)"
                elif remaining_distance > 100:
                    move_distance = 30
                    action = "MOVING FORWARD (Medium Speed)"
                else:
                    move_distance = 20
                    if remaining_distance <= 50 and not checkpoint_created:
                        self.add_checkpoint("Approach Zone")
                        checkpoint_created = True
                    action = "SLOWING DOWN (Approaching Target)"
            
            elif speed_status == "SLOW":
                if remaining_distance > 100:
                    move_distance = 10
                    action = "MOVING SLOWLY (Human Nearby)"
                else:
                    move_distance = 5
                    action = "MOVING VERY SLOWLY (Caution Zone)"
            
            else:  # CAUTIOUS or STOPPED
                if self.current_direction == "FORWARD":
                    move_distance = 15
                    action = "MOVING FORWARD (Cautiously)"
                elif self.current_direction == "LEFT":
                    move_distance = 12
                    action = "MOVING LEFT"
                elif self.current_direction == "RIGHT":
                    move_distance = 12
                    action = "MOVING RIGHT"
                elif self.current_direction == "BACK":
                    move_distance = 10
                    action = "MOVING BACKWARD"
                else:
                    move_distance = 0
                    action = "STOPPED"
            
            # Process movement
            if move_distance > 0:
                self.current_position += move_distance
                self.distance_travelled += move_distance
            else:
                self.current_position = self.target_distance
            
            # Check for unexpected changes
            unexpected = self.unexpected_change()
            
            # Check 50m signal
            self.check_50m_signal(remaining_distance)
            
            # Log movement
            status_msg = f"Step {movement_step}: {action} | Position: {min(self.current_position, self.target_distance)}m / {self.target_distance}m"
            print(status_msg)
            self.movement_log.append(status_msg)
            
            time.sleep(0.5)  # Small delay for simulation effect
            
            # Override if position exceeds target
            if self.current_position >= self.target_distance:
                self.current_position = self.target_distance
        
        return True
    
    def display_trip_summary(self):
        """Display complete trip summary using f-strings"""
        print(f"\n{'='*70}")
        print(f"📋 COMPREHENSIVE TRIP SUMMARY - {self.name.upper()}")
        print(f"{'='*70}\n")
        
        print(f"🤖 Robot Name: {self.name}")
        print(f"📍 Target Distance: {self.target_distance} meters")
        print(f"✓ Total Distance Travelled: {self.distance_travelled} meters")
        print(f"🎯 Destination Reached: {'YES ✓' if self.current_position >= self.target_distance else 'NO ✗'}")
        print(f"📊 Final Speed: {self.speed} km/h")
        print(f"🧭 Final Direction: {self.current_direction}")
        
        # Obstacle Status Information
        print(f"\n{'='*70}")
        print(f"⚠️  OBSTACLE STATUS & ENCOUNTERS")
        print(f"{'='*70}")
        print(f"Initial Obstacle Status: {self.obstacle_status}")
        print(f"Total Obstacles Encountered: {len(self.obstacles_encountered)}")
        
        if self.obstacles_encountered:
            print(f"\nObstacles Encountered List:")
            for i, obstacle in enumerate(self.obstacles_encountered, 1):
                print(f"  {i}. Type: {obstacle['type']} | Position: {obstacle['position']}m")
        else:
            print("  No obstacles encountered during journey ✓")
        
        # Checkpoints Information
        print(f"\n{'='*70}")
        print(f"✓ FINAL CHECKPOINT LIST ({len(self.checkpoints)} checkpoints)")
        print(f"{'='*70}")
        
        if self.checkpoints:
            print(f"{'ID':<5} {'Checkpoint Name':<25} {'Position':<12} {'Direction':<10}")
            print(f"{'-'*70}")
            for checkpoint in self.checkpoints:
                print(f"{checkpoint['id']:<5} {checkpoint['name']:<25} {checkpoint['position']:>10}m {checkpoint['direction']:<10}")
            
            # List operations summary
            print(f"\n📊 Checkpoint Operations Summary:")
            print(f"   • Total Checkpoints Added: {len(self.checkpoints)}")
            print(f"   • First Checkpoint: {self.checkpoints[0]['name']} at {self.checkpoints[0]['position']}m")
            if len(self.checkpoints) > 1:
                print(f"   • Last Checkpoint: {self.checkpoints[-1]['name']} at {self.checkpoints[-1]['position']}m")
        else:
            print("  No checkpoints recorded during journey")
        
        # Movement Summary
        print(f"\n{'='*70}")
        print(f"📍 MOVEMENT HISTORY ({len(self.movement_log)} total steps)")
        print(f"{'='*70}")
        print(f"Last 10 movements:")
        for i, log in enumerate(self.movement_log[-10:], 1):
            print(f"{i:2d}. {log}")
        
        # Final Journey Summary using f-strings
        print(f"\n{'='*70}")
        print(f"🎉 JOURNEY COMPLETE - FINAL REPORT")
        print(f"{'='*70}")
        
        journey_summary = f"""
╔════════════════════════════════════════════════════════════════╗
║                    ROBOCONTROLLER 1.0 REPORT                   ║
╠════════════════════════════════════════════════════════════════╣
║ Robot Name:            {self.name:<40} ║
║ Total Distance:        {self.distance_travelled} meters{' '*(35-len(str(self.distance_travelled)))} ║
║ Target Distance:       {self.target_distance} meters{' '*(35-len(str(self.target_distance)))} ║
║ Total Steps:           {len(self.movement_log):<40} ║
║ Checkpoints Created:   {len(self.checkpoints):<40} ║
║ Obstacles Encountered: {len(self.obstacles_encountered):<40} ║
║ Final Direction:       {self.current_direction:<40} ║
║ Journey Status:        {'SUCCESS ✓' if self.current_position >= self.target_distance else 'INCOMPLETE ✗':<40} ║
╚════════════════════════════════════════════════════════════════╝
        """
        print(journey_summary)
        print(f"{'='*70}\n")


def main():
    """Main program execution"""
    print("\n" + "="*60)
    print("🤖 ROBOCONTROLLER 1.0 - ROBOT MOVEMENT SIMULATOR")
    print("="*60 + "\n")
    
    # Get robot details from user
    robot_name = input("Enter robot name: ").strip()
    if not robot_name:
        robot_name = "RoboX"
    
    while True:
        try:
            target_distance = int(input("Enter target distance (in meters): ").strip())
            if target_distance > 0:
                break
            print("❌ Distance must be positive!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Create robot instance
    robot = Robot(robot_name, target_distance)
    
    # Simulate movement
    if robot.simulate_movement():
        # Display summary
        robot.display_trip_summary()
    else:
        print("\n❌ Journey failed to complete!")
        
    print("\n👋 Thank you for using RoboController 1.0!")


if __name__ == "__main__":
    main()
