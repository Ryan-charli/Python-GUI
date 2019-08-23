# PythonGUIDemo

> ![image.png](http://upload-images.jianshu.io/upload_images/3203841-d2c41b0319a26c49.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)






---




![软件界面](http://upload-images.jianshu.io/upload_images/3203841-4d125e0b232d8421.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


##### I compared pyqt5 with tkinter:

##### Pyqt5 has strong function and beautiful interface, but its grammar is complex. pyqt5 module needs to be installed separately, which is not suitable for beginners.

##### Tkinter is a module that comes with Python 3. It can meet the basic functional requirements, and its grammar is simple. It can be started in 5 minutes, so Tkinter is finally chosen.


#### Now most of the software versions are old, all for Python 2.7 programs, import methods such as `import Tkinter`,Python 3 should be`import tkinter`

### This time I chose a script named "Locating Geographical Location Based on IP Address" as the material, which is more interesting and easy to implement.






## The explanations are all in the comments. Here's the code:



```python
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
    

```
Operation effect:




> ![GIF](http://upload-images.jianshu.io/upload_images/3203841-53e9b6e7b63c6de0.gif?imageMogr2/auto-orient/strip)




> Because offline query IP requires global IP distribution data, so I directly chose a free offline query IP packet. In order to read the data of this packet, I also need to install a module:`pip install pygeoip`,When a few people installed Python 3, they chose the python 3 installation package without tkinter. In order to learn, they still need to add this module:`pip install tkinter`

