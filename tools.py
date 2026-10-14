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


class ControlPanel:
    def __init__(self):
        self.fractal_type = 0
        self.c_real = -0.8
        self.c_imag = 0.156
        self.max_iterations = 300

        self.is_animating = False
        self.anim_speed = 0.002
        self.dir_real = 1.0
        self.dir_imag = -1.0

    def _update_animation(self):
        if self.fractal_type == 0 and self.is_animating:
            self.c_real += self.anim_speed * self.dir_real
            self.c_imag += self.anim_speed * self.dir_imag
            
            if self.c_real >= 0.4 or self.c_real <= -1.4:
                self.dir_real *= -1.0
            if self.c_imag >= 0.8 or self.c_imag <= -0.8:
                self.dir_imag *= -1.0

    def update(self, gui, cam):
        self._update_animation()

        with gui.sub_window("Parametres de la Fractale", 0.02, 0.02, 0.32, 0.48) as w:
            w.text("Mode de rendu :")
            if w.button("Ensemble de Julia"):
                self.fractal_type = 0
                cam.reset(0)
            if w.button("Ensemble de Mandelbrot"):
                self.fractal_type = 1
                self.is_animating = False
                cam.reset(1)
                
            w.text("")
            self.max_iterations = w.slider_int("Iterations Max", self.max_iterations, 50, 5000)
            cam.palette = w.slider_int("Palette (ou touche C)", cam.palette, 0, 4)
            
            if self.fractal_type == 0:
                w.text("")
                w.text("Constante C (Temps reel) :")
                self.c_real = w.slider_float("C Reel (X)", self.c_real, -2.0, 2.0)
                self.c_imag = w.slider_float("C Imag (Y)", self.c_imag, -2.0, 2.0)
                
                w.text("")
                btn_label = "Pause Animation" if self.is_animating else "Lancer Animation"
                if w.button(btn_label):
                    self.is_animating = not self.is_animating
                    
                self.anim_speed = w.slider_float("Vitesse Anim", self.anim_speed, 0.0005, 0.01)
                
            w.text("")
            w.text("Navigation : Clic Droit = Bouger | A/E = Zoom")