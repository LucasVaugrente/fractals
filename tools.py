import taichi as ti

class Camera:
    def __init__(self):
        self.zoom = 1.0
        self.offset_x = 0.0
        self.offset_y = 0.0
        
        self.is_dragging = False
        self.last_mouse_pos = (0.0, 0.0)
        
        self.palette = 0
        self.c_pressed = False

    def reset(self, fractal_type=0):
        self.zoom = 1.0
        self.offset_x = -0.5 if fractal_type == 1 else 0.0
        self.offset_y = 0.0

    def handle_input(self, window):
        mouse_pos = window.get_cursor_pos()
        win_w, win_h = window.get_window_shape()
        aspect_ratio = win_w / max(1, win_h)
        
        if window.is_pressed(ti.ui.RMB):
            if not self.is_dragging:
                self.is_dragging = True
                self.last_mouse_pos = mouse_pos
            else:
                dmx = mouse_pos[0] - self.last_mouse_pos[0]
                dmy = mouse_pos[1] - self.last_mouse_pos[1]
                
                self.offset_x -= dmx * 2.0 * aspect_ratio * self.zoom
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
            
            if new_zoom >= 1.0:
                new_zoom = 1.0
                self.offset_x = 0.0
                self.offset_y = 0.0
            elif new_zoom != self.zoom:
                px = (mouse_pos[0] - 0.5) * 2.0 * aspect_ratio
                py = (mouse_pos[1] - 0.5) * 2.0
                
                self.offset_x += px * (self.zoom - new_zoom)
                self.offset_y += py * (self.zoom - new_zoom)
            
            self.zoom = new_zoom
            
        if window.is_pressed('c'):
            if not self.c_pressed:
                self.palette = (self.palette + 1) % 5
                self.c_pressed = True
        else:
            self.c_pressed = False
            
        return aspect_ratio