import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Load car images
car1_image = cv2.imread("car1.png")
car2_image = cv2.imread("car2.png")

class Car:
    def __init__(self, lane):
        self.lane = lane
        self.position = 0
        self.message = None
    
    def move(self):
        self.position += 1
    
    def change_lane(self, other_car):
        if self.lane != other_car.lane:
            self.message = "Don't change lane!"

def visualize_cars(car1, car2):
    lanes = ["Lane 1", "Lane 2"]
    
    plt.figure(figsize=(10, 5))
    plt.xlim(0, 10)
    plt.ylim(0, len(lanes))
    plt.xticks([])
    plt.yticks([])
    
    for i, lane in enumerate(lanes):
        plt.axhline(y=i+0.5, color='gray', linestyle='--')
        plt.text(-0.5, i+0.5, lane, ha="center", va="center")
    
    plt.imshow(car1_image, extent=[car1.position-0.5, car1.position+0.5, 1, 2])
    plt.imshow(car2_image, extent=[car2.position-0.5, car2.position+0.5, 0, 1])
    
    while car1.position < 10:
        car1.move()
        car2.move()
        
        if car1.position == 3:
            car1.change_lane(car2)
        
        plt.clf()
        plt.xlim(0, 10)
        plt.ylim(0, len(lanes))
        plt.xticks([])
        plt.yticks([])
        arrow = patches.Arrow(car2.position + 0.5, 0.5, 0, 0.4, width=0.2, color='red')
        plt.gca().add_patch(arrow)
        for i, lane in enumerate(lanes):
            plt.axhline(y=i+0.5, color='gray', linestyle='--')
            plt.text(-0.5, i+0.5, lane, ha="center", va="center")
        
        plt.imshow(car1_image, extent=[car1.position-0.5, car1.position+0.5, 1, 2])
        plt.imshow(car2_image, extent=[car2.position-0.5, car2.position+0.5, 0, 1])
        
        if car1.message is not None:
            plt.text(car1.position, 2.2, car1.message, ha="center", va="bottom", color='red')
        
        plt.pause(0.5)
    
    plt.show()

car1 = Car(lane=1)
car2 = Car(lane=2)

visualize_cars(car1, car2)
