# Create a class paper with width and height as data Member. 
# Create function outside aclass that find out area and perimeter 
# of that paper Pass object argument.
# area=width*height, perimeter=2*(width+height)

class Paper:
    def __init__(self, width, height): # __init__ here is basically a constructor
        # self refers to the object being created
        self.width = width
        self.height = height
    
def calculate_details(paper_object):
    area = paper_object.width * paper_object.height

    perimeter = 2 * (paper_object.width + paper_object.height)

    print(f" ----- Paper Ananlysis ----- ")
    print(f" Width: {paper_object.width}")
    print(f" Height: {paper_object.height}")
    print(f" Area: {area}")
    print(f" Perimeter: {perimeter}")

a4_paper = Paper(8.5, 11)

calculate_details(a4_paper)
