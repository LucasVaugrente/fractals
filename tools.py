import taichi as ti

class Camera:
    def __init__(self, res_x, res_y):
        self.zoom = 1.0
        self.offset_x = 0.0
        self.offset_y = 0.0
        
        self.res_x = res_x
        self.res_y = res_y
        
        self.is_dragging = False
        self.last_mouse_pos = (0.0, 0.0)
        
        self.palette = 0
        self.c_pressed = False

    def handle_input(self, window):
        mouse_pos = window.get_cursor_pos() 
        
        if window.is_pressed(ti.ui.LMB):
            if not self.is_dragging:
                self.is_dragging = True
                self.last_mouse_pos = mouse_pos
            else:
                dmx = mouse_pos[0] - self.last_mouse_pos[0]
                dmy = mouse_pos[1] - self.last_mouse_pos[1]
                
                self.offset_x -= dmx * 2.0 * (self.res_x / self.res_y) * self.zoom
                self.offset_y -= dmy * 2.0 * self.zoom
                
                self.last_mouse_pos = mouse_pos
        else:
            self.is_dragging = False

        zoom_factor = 1.0
        if window.is_pressed('a'):
            zoom_factor = 0.95
        elif window.is_pressed('e'):
            zoom_factor = 1.05
            
        if zoom_factor != 1.0:
            new_zoom = self.zoom * zoom_factor
            
            if new_zoom >= 1.5:
                new_zoom = 1.5
            
            elif new_zoom != self.zoom:
                px = (mouse_pos[0] - 0.5) * 2.0 * (self.res_x / self.res_y)
                py = (mouse_pos[1] - 0.5) * 2.0
                
                self.offset_x += px * (self.zoom - new_zoom)
                self.offset_y += py * (self.zoom - new_zoom)
            
            self.zoom = new_zoom
            
        if window.is_pressed('c'):
            if not self.c_pressed:
                self.palette = (self.palette + 1) % 4
                self.c_pressed = True
        else:
            self.c_pressed = False