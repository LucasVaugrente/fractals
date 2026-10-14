import taichi as ti
from tools import Camera, ControlPanel
from fractals.julia import render_julia
from fractals.mandelbrot import render_mandelbrot

ti.init(arch=ti.gpu)

buf_x, buf_y = 1920, 1080
pixels = ti.Vector.field(n=3, dtype=ti.f32, shape=(buf_x, buf_y))

window = ti.ui.Window("Explorateur de Fractales (GPU)", (1200, 800), vsync=True)
canvas = window.get_canvas()
gui = window.get_gui()

cam = Camera()
panel = ControlPanel()

while window.running:
    aspect_ratio = cam.handle_input(window)
    panel.update(gui, cam)

    if panel.fractal_type == 0:
        render_julia(
            pixels, buf_x, buf_y, aspect_ratio, 
            panel.c_real, panel.c_imag, 
            cam.zoom, cam.offset_x, cam.offset_y, 
            panel.max_iterations, cam.palette
        )
    else:
        render_mandelbrot(
            pixels, buf_x, buf_y, aspect_ratio, 
            cam.zoom, cam.offset_x, cam.offset_y, 
            panel.max_iterations, cam.palette
        )
    
    canvas.set_image(pixels)
    window.show()