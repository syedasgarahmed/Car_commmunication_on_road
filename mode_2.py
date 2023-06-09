import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

class Vehicle:
    def __init__(self, name, lane, position):
        self.name = name
        self.lane = lane
        self.position = position
        self.is_stopped = False
    
    def move(self, distance):
        if self.is_stopped:
            print(f'{self.name} in lane {self.lane} is stopped.')
        else:
            self.position += distance
            print(f'{self.name} in lane {self.lane} is at position {self.position} on the road.')

class Person:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.current_lane = 0
        self.is_crossing = False
    
    def move(self, distance):
        self.position += distance
        print(f'{self.name} is at position {self.position}.')
        
    def start_crossing(self):
        self.is_crossing = True
    
    def stop_crossing(self):
        self.is_crossing = False

# Road parameters
road_length = 10
num_lanes = 3

# Create car and person instances
car = Vehicle('Car', lane=1, position=0)
person = Person('Person', position=0)

# Create figure and axis
fig, ax = plt.subplots()

# Plot road and lanes
ax.plot([0, road_length], [0, 0], 'k-', lw=3)
ax.plot([0, road_length], [num_lanes, num_lanes], 'k-', lw=3)
for lane in range(1, num_lanes):
    ax.plot([0, road_length], [lane, lane], 'k--', lw=1)

# Add image placeholders for car and person
car_image = plt.imread('car_image.png')  # Replace 'car_image.png' with the actual car image file
person_image = plt.imread('person_image.png')  # Replace 'person_image.png' with the actual person image file

# Plot car
car_marker = ax.imshow(car_image, extent=[car.position - 0.5, car.position + 0.5, car.lane - 0.5, car.lane + 0.5])

# Plot person
person_marker = ax.imshow(person_image, extent=[person.position - 0.5, person.position + 0.5, person.current_lane - 0.5, person.current_lane + 0.5])

# Set plot limits and labels
ax.set_xlim([-1, road_length + 1])
ax.set_ylim([-0.5, num_lanes + 0.5])
ax.set_xlabel('Position')
ax.set_ylabel('Lane')
ax.set_title('Road Interaction')

# Create a text object for displaying messages
message_text = ax.text(0.5, num_lanes - 0.5, '', ha='center', va='center', fontsize=12, color='red')

# Update function for animation
def update(frame):
    car.move(0.05)  # Move the car (adjust speed as needed)
    person.move(0.05)  # Move the person (adjust speed as needed)
    
    if car.position >= 4 and not person.is_crossing:
        car.is_stopped = True
        print(f'{car.name} in lane {car.lane} stopped to allow {person.name} to cross the road.')
        message_text.set_text('                                             car: Carefully cross the road.')
        if person.position>5 and person.position<6:
            message_text.set_text('                                             person: okay!')
        if car.position>6:
            message_text.set_text('                                             ')
       # time.sleep(3)
        #message_text.set_text('                                             person: okay!')
        
    if person.current_lane>2 and person.position>5:
        #time.sleep(4)
        car.is_stopped=False
        
    if person.position >= 4.3 and person.current_lane == 0:
        person.current_lane = 3
        print(f'{person.name} moved to lane 2.')
    
    if person.position >= road_length:
        person.stop_crossing()
        print(f'{person.name} finished crossing the road.')
        message_text.set_text('')
        car.is_stopped = False
    
    # Update car position in the graph
    car_marker.set_extent([car.position - 0.5, car.position + 0.5, car.lane - 0.5, car.lane + 0.5])
    
    # Update person position in the graph
    person_marker.set_extent([person.position - 0.5, person.position + 0.5, person.current_lane - 0.5, person.current_lane + 0.5])

    return car_marker, person_marker, message_text

# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=100, blit=True)

# Display the animation
plt.show()
