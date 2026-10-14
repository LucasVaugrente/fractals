import taichi as ti
from tools import Camera
from fractals.julia import render_julia
from fractals.mandelbrot import render_mandelbrot

ti.init(arch=ti.gpu)

buf_x, buf_y = 1920, 1080
pixels = ti.Vector.field(n=3, dtype=ti.f32, shape=(buf_x, buf_y))

fractal_type = 0
c_real = -0.8
c_imag = 0.156
max_iterations = 300

window = ti.ui.Window("Explorateur de Fractales (GPU)", (1200, 800), vsync=True)
canvas = window.get_canvas()
gui = window.get_gui()
cam = Camera()

while window.running:
    aspect_ratio = cam.handle_input(window)
    
    with gui.sub_window("Parametres de la Fractale", 0.02, 0.02, 0.32, 0.36) as w:
        w.text("Mode de rendu :")
        if w.button("Ensemble de Julia"):
            fractal_type = 0
            cam.reset(0)
        if w.button("Ensemble de Mandelbrot"):
            fractal_type = 1
            cam.reset(1)
            
        w.text("")
        max_iterations = w.slider_int("Iterations Max", max_iterations, 50, 5000)
        
        cam.palette = w.slider_int("Palette (ou touche C)", cam.palette, 0, 4)
        
        if fractal_type == 0:
            w.text("")
            w.text("Constante C (Temps reel) :")
            c_real = w.slider_float("C Reel (X)", c_real, -2.0, 2.0)
            c_imag = w.slider_float("C Imag (Y)", c_imag, -2.0, 2.0)
            
        w.text("")
        w.text("Navigation : Clic Droit = Bouger | A/E = Zoom")

    if fractal_type == 0:
        render_julia(pixels, buf_x, buf_y, aspect_ratio, c_real, c_imag, cam.zoom, cam.offset_x, cam.offset_y, max_iterations, cam.palette)
    else:
        render_mandelbrot(pixels, buf_x, buf_y, aspect_ratio, cam.zoom, cam.offset_x, cam.offset_y, max_iterations, cam.palette)
    
    canvas.set_image(pixels)
    window.show()