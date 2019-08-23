import tkinter
import pygeoip

class FindLocation(object):
    def __init__(self):
        self.gi = pygeoip.GeoIP("./GeoLiteCity.dat")
        # Create a main window to accommodate other components
        self.root = tkinter.Tk()
        # Set the title content for the main window
        self.root.title("Global positioning IP location (offline version)")
        # Create an input box and set the size
        self.ip_input = tkinter.Entry(self.root,width=30)

        # Create an echo list
        self.display_info = tkinter.Listbox(self.root, width=50)

        # Create a button for query results
        self.result_button = tkinter.Button(self.root, command = self.find_position, text = "Check")

    # Complete the layout
    def gui_arrang(self):
        self.ip_input.pack()
        self.display_info.pack()
        self.result_button.pack()

    # Find geographic location based on IP
    def find_position(self):
        # Get input information
        self.ip_addr = self.ip_input.get()
        aim = self.gi.record_by_name(self.ip_addr)
        
        try:

            # Acquisition of target cities
            city = aim["city"]
            # Acquisition of target countries
            country = aim["country_name"]
            # Acquisition of target areas
            region_code = aim["region_code"]
            # Obtaining the longitude of the target
            longitude = aim["longitude"]
            # Acquire target latitude
            latitude = aim["latitude"]
        except:
            pass
        
        # Create temporary lists
        the_ip_info = ["Latitude:"+str(latitude),"Longitude:"+str(longitude),"Regional code:"+str(region_code),"City:"+str(city), "Country or region:"+str(country), "IP:"+str(self.ip_addr)]
        #Clear the visible part of the echo list, similar to the clear command
        for item in range(10):
            self.display_info.insert(0,"")

        # Assign values to the echo list
        for item in the_ip_info:
            self.display_info.insert(0,item)
        
        return the_ip_info


def main():
    # Initialization object
    FL = FindLocation()
    # Layout
    FL.gui_arrang()
    # Main program execution
    tkinter.mainloop()
    pass


if __name__ == "__main__":
    main()
