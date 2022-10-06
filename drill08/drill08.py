from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir1, dir2

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir1 += 1
            elif event.key == SDLK_LEFT:
                dir1 -= 1
            if event.key == SDLK_UP:
                dir2 += 1
            elif event.key == SDLK_DOWN:
                dir2 -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir1 -= 1
            elif event.key == SDLK_LEFT:
                dir1 += 1
            if event.key == SDLK_UP:
                dir2 -= 1
            elif event.key == SDLK_DOWN:
                dir2 += 1
    pass

open_canvas()
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 1280 // 2
y = 1024 // 2
frame = 0
dir1, dir2 = 0, 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir1 * 5
    # character.clip_draw(frame * 100, 100 * a, 100, 100, x, y)
    #a=1
    y += dir2 * 5
    # character.clip_draw(frame * 100, 100 * a, 100, 100, x, y)
    #a=2
    delay(0.01)

close_canvas()
