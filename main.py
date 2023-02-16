import pygame
import random
from terrain_handler import Chunk 
from animation import Idle
import sys
from render import Render
import time
import math
from entities import Entity, Player, Enemy, Player_Projectile, Lava_Drop_Projectile
from ui import Button, Image_Button, Text, Display_Image
from pathfinding import PathFinder

pygame.init()
render = Render()

clock = pygame.time.Clock()
FRAME_RATE = 30

blob_img = render.scale_texture_normal(pygame.image.load('Images/blob_right.png'))
blob_down_img = render.scale_texture_normal(pygame.image.load('Images/blob_down_right.png'))
full_size_blob = render.scale_texture_large(pygame.image.load('Images/blob_right.png'))
crying_blob_img = render.scale_texture_large(pygame.image.load('Images/blob_crying.png'))
crying_blob_2_img = render.scale_texture_large(pygame.image.load('Images/blob_crying_2.png'))
blob_celebration_1_img = render.scale_texture_large(pygame.image.load('Images/blob_right_celebration_1.png'))
blob_celebration_2_img = render.scale_texture_large(pygame.image.load('Images/blob_right_celebration_2.png'))

pygame.display.set_caption("The Adventures of Lil' Herb")
pygame.display.set_icon(blob_img)

for i in range(len(render.LEVEL_MAP_NUMBERS)):
    render.level_row()

mode = "Level"

def ray_march(current_position, direction):
    pixels_traveled = 0
    max_pixels = 16
    while (get_block(current_position) in render.traversable_blocks) and pixels_traveled <= max_pixels:
        pixels_traveled += 1
        current_position[0] += direction[0]
        current_position[1] += direction[1]
    return pixels_traveled

def get_player_location():
    return game_entities[0].get_world_position()

def get_entity_location(position_in_list):
    return game_entities[position_in_list].position

def get_block(current_position):
    current_block_size = render.BLOCK_SIZE

    horizontal_offset = (render.movement_horizontal * current_block_size)
    vertical_offset = (render.movement_vertical * current_block_size)

    actual_x_pos = math.floor((current_position[0] - horizontal_offset) / current_block_size)
    actual_y_pos = math.floor((current_position[1] - vertical_offset) / current_block_size)

    chunk_coords = (math.floor(actual_x_pos / 8), math.floor(actual_y_pos / 8))
    block_within_chunk_coords = (int((actual_x_pos / 8 - chunk_coords[0]) * 8), int((actual_y_pos / 8 - chunk_coords[1]) * 8))

    block = render.LEVEL_MAP[chunk_coords[0] * 4 + chunk_coords[1]].CHUNK[block_within_chunk_coords[1]][block_within_chunk_coords[0]]
    return block

def get_block_coords(position):
    current_block_size = render.BLOCK_SIZE

    horizontal_offset = (render.movement_horizontal * current_block_size)
    vertical_offset = (render.movement_vertical * current_block_size)

    actual_x_pos = math.floor((position[0] - horizontal_offset) / current_block_size)
    actual_y_pos = math.floor((position[1] - vertical_offset) / current_block_size)

    chunk_coords = (math.floor(actual_x_pos / 8), math.floor(actual_y_pos / 8))
    block_within_chunk_coords = (int((actual_x_pos / 8 - chunk_coords[0]) * 8), int((actual_y_pos / 8 - chunk_coords[1]) * 8))
    return chunk_coords, block_within_chunk_coords

game_entities = []
level_music = {0 : "Audio/Time.mp3",
                1 : "Audio/Mist.mp3"}

def check_entity_collisions():
    for entity in game_entities:
        if entity.entity_type == "Player":
            pos = [entity.position[0] + render.movement_horizontal * -32, entity.position[1]]
        else:
            pos = [entity.position[0], entity.position[1]]
        for other_entity in game_entities:
            if entity != other_entity:
                if other_entity.entity_type == "Player":
                    other_pos = [other_entity.position[0] + render.movement_horizontal * -32, other_entity.position[1]]
                else:
                    other_pos = [other_entity.position[0],  other_entity.position[1]]

                if within_10_px(pos, other_pos):
                    entity.on_collide(other_entity)
                    other_entity.on_collide(entity)

def within_10_px(entity1, entity2):
    return abs(entity1[0] - entity2[0]) < 10 and abs(entity1[1] - entity2[1]) < 10

def update_enemy_list_positions():
    for entity in game_entities:
        if entity.entity_type == "Enemy":
            game_entities[game_entities.index(entity)].entity_num = game_entities.index(entity)

def time_taken_to_complete(start_time, end_time):
    time_elapsed = end_time - start_time
    minutes = round(time_elapsed // 60)
    seconds = round((time_elapsed % 60), 2)
    minutes_seconds = [minutes, seconds]
    return minutes_seconds

def on_screen_timer(start_time):
    current_time = time.time()
    time_elapsed = current_time - start_time
    minutes = round(time_elapsed // 60)
    seconds = round((time_elapsed % 60), 2)
    minutes_seconds = [minutes, seconds]
    return minutes_seconds

def Game_Screen(level):
    render.convert_map_list_to_level(render.file.load(level))
    render.find_start()
    render.find_finish()
    enemy_spawn_coords = render.find_enemy_spawn_points()
    lava_drop_block_coords = render.find_lava_drop_spawners()
    running = True

    game_entities.append(Player(1024, render.start_coords[1] * render.BLOCK_SIZE, render, ray_march, get_player_location, get_block_coords, get_entity_location, get_block, level))
    for i in range(len(enemy_spawn_coords)):
        enemy = Enemy(enemy_spawn_coords[i][0] * render.BLOCK_SIZE, enemy_spawn_coords[i][1] * render.BLOCK_SIZE, render, ray_march, get_player_location, get_block_coords, get_entity_location, get_block, level)
        game_entities.append(enemy)
        game_entities[game_entities.index(enemy)].entity_num = game_entities.index(enemy)

        

    render.music.load(level_music[level])
    render.music.play(-1)

    count = 0

    render.movement_horizontal = -render.start_coords[0] + 32

    timer = Text(render, (0,0,205), f"0 Minutes and 0.00 Seconds!", 20, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 400))
    

    start_time = time.time()
    while running:
        if count == 0:
            render.draw_level()
            render.draw_level()
            
        count += 1
        check_entity_collisions()

        render.wipe()
        render.draw_level()

        current_timer = on_screen_timer(start_time)
        timer = Text(render, (0,0,205), f"{current_timer[0]} Minutes and {current_timer[1]} Seconds!", 20, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 400))
        timer.paste_text()

        #Lava drop timer 
        if count % 35 == 0:
            for i in range(len(lava_drop_block_coords)):
                drop = Lava_Drop_Projectile(lava_drop_block_coords[i][0] * render.BLOCK_SIZE, lava_drop_block_coords[i][1] * render.BLOCK_SIZE, render, ray_march, get_player_location, get_block_coords, get_entity_location, get_block, level)
                game_entities.append(drop)

        for entity in game_entities:
            texture = entity.get_texture()
            position = entity.position

            if entity == game_entities[0]: 
                if entity.dead == True:
                    game_entities.clear()
                    Level_Failed_Screen(level)
                    running = False
                elif entity.finished == True:
                    end_time = time.time()
                    game_entities.clear()
                    Level_Completed_Screen(level, time_taken_to_complete(start_time, end_time))
                    running = False
                else:
                    render.screen.blit(texture, position)
                
            else:
                '''print((entity.position[0] + render.movement_horizontal * render.BLOCK_SIZE, entity.position[1] + render.movement_vertical * render.BLOCK_SIZE))'''
                if entity.dead == True:
                    if entity.entity_type == "Enemy":
                        
                        game_entities.remove(entity)
                        update_enemy_list_positions()
                        
                        print("Enemy removed")
                        for entity in game_entities:
                            if entity.entity_type == "Enemy" and entity.shot == False:
                                render.screen.blit(entity.get_texture(), (entity.position[0] + render.movement_horizontal * render.BLOCK_SIZE, entity.position[1] + render.movement_vertical * render.BLOCK_SIZE))
                    else:
                        game_entities.remove(entity)
                        print("Entity removed")
                else:
                    render.screen.blit(texture, (entity.position[0] + render.movement_horizontal * render.BLOCK_SIZE, entity.position[1] + render.movement_vertical * render.BLOCK_SIZE))
            
        for entity in game_entities:
            entity.tick()
            

        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                for entity in game_entities:
                    entity.on_key_press(event.key)

            if event.type == pygame.KEYUP:
                for entity in game_entities:
                    entity.on_key_release(event.key)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_entities[0].on_mouse_button_click(event.button) == True:
                    if game_entities[0].state == 0 or game_entities[0].state == 2:
                        projectile = Player_Projectile(game_entities[0].position[0] - render.movement_horizontal * render.BLOCK_SIZE + 8, game_entities[0].position[1] + 6, render, ray_march, get_player_location, get_block_coords, get_entity_location, get_block, level)
                        #RIGHT
                        projectile.direction = True
                        game_entities.append(projectile)
                    else:
                        projectile = Player_Projectile(game_entities[0].position[0] - render.movement_horizontal * render.BLOCK_SIZE - 8, game_entities[0].position[1] + 6, render, ray_march, get_player_location, get_block_coords, get_entity_location, get_block, level)
                        #LEFT
                        projectile.direction = False
                        game_entities.append(projectile)
                
                
        
        pygame.display.update()
        clock.tick(FRAME_RATE)
        #print(clock.get_fps())

def Options_Screen():
    displayed = True
    render.screen.blit(render.BG, (0,0))

    volume_up_button = Button(render, (0,0,205), (0,0,139), (0,0,0), "+", (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 200))
    volume_down_button = Button(render, (0,0,205), (0,0,139), (0,0,0), "-", (render.WINDOW_WIDTH/2 + 150,render.WINDOW_HEIGHT/2 - 200))

    back_button = Button(render, (0,0,205), (0,0,139), (0,0,0), "Back", (150,100))

    title = Text(render, (0,0,205), "Options:", 80, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 350))
    volume = Text(render, (0,0,205), f"Volume: {int(render.music_volume * 10)}", 60, (render.WINDOW_WIDTH/2 - 300,render.WINDOW_HEIGHT/2 - 200))

    while displayed:
        render.screen.blit(render.BG, (0,0))

        volume_up_button.change_button_colour(pygame.mouse.get_pos())
        volume_up_button.button_update()

        volume_down_button.change_button_colour(pygame.mouse.get_pos())
        volume_down_button.button_update()

        back_button.change_button_colour(pygame.mouse.get_pos())
        back_button.button_update()
    
        title.paste_text()
        volume.paste_text()

        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                displayed = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if volume_up_button.check_clicked(pygame.mouse.get_pos()) == True:
                    if render.music_volume >= 1:
                        pass
                    else:
                        render.music_volume += 0.1
                        render.music.set_volume(render.music_volume)
                        volume = Text(render, (0,0,205), f"Volume: {int(render.music_volume * 10)}", 60, (render.WINDOW_WIDTH/2 - 300,render.WINDOW_HEIGHT/2 - 200))

                if volume_down_button.check_clicked(pygame.mouse.get_pos()) == True:
                    if render.music_volume <= 0.1:
                        pass
                    else:
                        render.music_volume -= 0.1
                        render.music.set_volume(render.music_volume)
                        volume = Text(render, (0,0,205), f"Volume: {int(render.music_volume * 10)}", 60, (render.WINDOW_WIDTH/2 - 300,render.WINDOW_HEIGHT/2 - 200))
                
                if back_button.check_clicked(pygame.mouse.get_pos()) == True:
                    Start_Screen()
                    displayed = False

        pygame.display.update()
        clock.tick(FRAME_RATE)

def Start_Screen():
    displayed = True
    render.screen.blit(render.BG, (0,0))

    game_title = Text(render, (0,0,205), "The Adventures of Lil' Herb", 120, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 350))
    start_button = Button(render, (0,0,205), (0,0,139), (0,0,0), "Play", (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2))
    options_button = Button(render, (0,0,205), (0,0,139), (0,0,0), "Options", (render.WINDOW_WIDTH/2 - 150,render.WINDOW_HEIGHT/2 + 150))
    help_button = Button(render, (0,0,205), (0,0,139), (0,0,0), "Help", (render.WINDOW_WIDTH/2 + 175,render.WINDOW_HEIGHT/2 + 150))
    quit_button = Button(render, (0,0,205), (0,0,139), (0,0,0), "Quit", (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 + 300))

    blob = Display_Image(render, blob_img, (render.WINDOW_WIDTH/2 - 740,render.WINDOW_HEIGHT/2 - 404))
    blob_down = Display_Image(render, blob_down_img, (render.WINDOW_WIDTH/2 - 740,render.WINDOW_HEIGHT/2 - 404))

    count = 0
    state = 0

    while displayed:
        if count % 10 == 0:
            if state == 0:
                state = 1
            else:
                state = 0
                
        render.wipe()
        render.screen.blit(render.BG, (0,0))

        start_button.change_button_colour(pygame.mouse.get_pos())
        start_button.button_update()

        options_button.change_button_colour(pygame.mouse.get_pos())
        options_button.button_update()

        help_button.change_button_colour(pygame.mouse.get_pos())
        help_button.button_update()

        quit_button.change_button_colour(pygame.mouse.get_pos())
        quit_button.button_update()

        game_title.paste_text()

        if state == 0:
            blob.paste_img()
        else:
            blob_down.paste_img()

        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                displayed = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.check_clicked(pygame.mouse.get_pos()) == True:
                    Level_Selection_Screen()
                    displayed = False
                if options_button.check_clicked(pygame.mouse.get_pos()) == True:
                    Options_Screen()
                    displayed = False
                if help_button.check_clicked(pygame.mouse.get_pos()) == True:
                    Help_Screen()
                    displayed = False
                if quit_button.check_clicked(pygame.mouse.get_pos()) == True:
                    displayed = False

        
        pygame.display.update()
        count += 1
        clock.tick(FRAME_RATE)

def Level_Selection_Screen():
    displayed = True
    render.screen.blit(render.BG, (0,0))

    back_button = Button(render, (0,0,205), (0,0,139), (0,0,0), "Back", (150,100))
    
    level_1 = Button(render, (0,0,205), (0,0,139), (0,0,0), "Level 1: Dangerous Caverns", (700, 250))
    level_2 = Button(render, (0,0,205), (0,0,139), (0,0,0), "Level 2: Toasty Hollows", (585, 325))

    title = Text(render, (0,0,205), "Level Selection:", 80, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 350))
    

    while displayed:
        back_button.change_button_colour(pygame.mouse.get_pos())
        back_button.button_update()

        level_1.change_button_colour(pygame.mouse.get_pos())
        level_1.button_update()

        level_2.change_button_colour(pygame.mouse.get_pos())
        level_2.button_update()

        title.paste_text()
    


        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                displayed = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_clicked(pygame.mouse.get_pos()) == True:
                    Start_Screen()
                    displayed = False
                if level_1.check_clicked(pygame.mouse.get_pos()) == True:
                    Game_Screen(0)
                    displayed = False
                if level_2.check_clicked(pygame.mouse.get_pos()) == True:
                    Game_Screen(1)
                    displayed = False

        
        pygame.display.update()
        clock.tick(FRAME_RATE)

def Help_Screen():
    displayed = True
    render.screen.blit(render.BG, (0,0))

    back_button = Button(render, (0,0,205), (0,0,139), (0,0,0), "Back", (150,100))
    
    #image_test = Image_Button(render, pygame.image.load('Images/grass.png').convert(), (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2))
    
    title = Text(render, (0,0,205), "How to play:", 80, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 350))
    subtitle_movement = Text(render, (0,0,205), "Controls:", 60, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 200))
    movement_text_right = Text(render, (0,0,205), "Right: press and hold the 'D' key", 40, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 150))
    movement_text_left = Text(render, (0,0,205), "Left: press and hold the 'A' key", 40, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 100))
    movement_text_jump = Text(render, (0,0,205), "Jump: press and release the 'SPACE' key", 40, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 50))
    movement_text_shoot = Text(render, (0,0,205), "Shoot: 'Left Mouse' button click then release", 40, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2))
    subtitle_objective = Text(render, (0,0,205), "Objective:", 60, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 + 100))
    main_objective = Text(render, (0,0,205), "The main goal of the game, is to reach the finish line while avoiding dangers", 40, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 + 150))
    dangers = Text(render, (0,0,205), "Dangers consist of deep pits, enemy characters and blocks that can kill you", 40, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 + 200))
    enemies = Text(render, (0,0,205), "Enemies will try to stop you from completing the level by attacking you", 40, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 + 250))
    finish_line = Text(render, (0,0,205), "Reach the finish line to complete the level", 40, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 + 300))

    while displayed:
        back_button.change_button_colour(pygame.mouse.get_pos())
        back_button.button_update()

        #image_test.button_update()
        title.paste_text()
        subtitle_movement.paste_text()
        movement_text_right.paste_text()
        movement_text_left.paste_text()
        movement_text_jump.paste_text()
        movement_text_shoot.paste_text()
        subtitle_objective.paste_text()
        main_objective.paste_text()
        dangers.paste_text()
        enemies.paste_text()
        finish_line.paste_text()

        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                displayed = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_clicked(pygame.mouse.get_pos()) == True:
                    Start_Screen()
                    displayed = False
                #if image_test.check_clicked(pygame.mouse.get_pos()) == True:
                    #Game_Screen(0)
                    #displayed = False

        
        pygame.display.update()
        clock.tick(FRAME_RATE)

def Level_Failed_Screen(level):
    render.music.load('Audio/Darkness.mp3')
    render.music.set_volume(render.music_volume)
    render.music.play(-1)
    displayed = True

    render.screen.blit(render.BG, (0,0))    
    back_to_main_button = Button(render, (0,0,205), (0,0,139), (0,0,0), "Back To Main Menu", (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 + 300))
    retry_level = Button(render, (0,0,205), (0,0,139), (0,0,0), "Retry Level", (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 + 150))
    
    crying_blob = Display_Image(render, crying_blob_img, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 150))
    crying_blob_2 = Display_Image(render, crying_blob_2_img, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 150))
    title = Text(render, (255,0,0), "Level Failed! You Died!", 80, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 350))

    count = 0
    state = 0

    while displayed:
        render.wipe()
        render.screen.blit(render.BG, (0,0))
        if count % 10 == 0:
            if state == 0:
                state = 1
            else:
                state = 0
        
        if state == 1:
            crying_blob.paste_img()
        else:
            crying_blob_2.paste_img()
            
        back_to_main_button.change_button_colour(pygame.mouse.get_pos())
        back_to_main_button.button_update()

        retry_level.change_button_colour(pygame.mouse.get_pos())
        retry_level.button_update()

        title.paste_text()

        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                displayed = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_to_main_button.check_clicked(pygame.mouse.get_pos()) == True:
                    Start_Screen()
                    displayed = False
                if retry_level.check_clicked(pygame.mouse.get_pos()) == True:
                    Game_Screen(level)
                    displayed = False


        
        pygame.display.update()
        clock.tick(FRAME_RATE)
        
        count += 1

def Level_Completed_Screen(level, time_to_complete):
    displayed = True
    render.screen.blit(render.BG, (0,0))

    back_to_main_button = Button(render, (0,0,205), (0,0,139), (0,0,0), "Back To Main Menu", (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 + 300))
    play_level_again = Button(render, (0,0,205), (0,0,139), (0,0,0), "Play Level Again", (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 + 150))
    
    blob_celebration_1 = Display_Image(render, blob_celebration_1_img, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 150))
    blob_celebration_2 = Display_Image(render, blob_celebration_2_img, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 150))
    title = Text(render, (0,0,205), "Level Completed!", 80, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 - 350))
    time_taken = Text(render, (0,0,205), f"Time taken to complete: {time_to_complete[0]} Minutes and {time_to_complete[1]} Seconds!", 30, (render.WINDOW_WIDTH/2,render.WINDOW_HEIGHT/2 + 75))
    
    count = 0
    state = 0

    while displayed:
        render.wipe()
        render.screen.blit(render.BG, (0,0))
        if count % 40 == 0:
            if state == 0:
                state = 1
            else:
                state = 0
        
        if state == 1:
            blob_celebration_1.paste_img()
        else:
            blob_celebration_2.paste_img()
        
        count += 1

        back_to_main_button.change_button_colour(pygame.mouse.get_pos())
        back_to_main_button.button_update()

        play_level_again.change_button_colour(pygame.mouse.get_pos())
        play_level_again.button_update()

        title.paste_text()
        time_taken.paste_text()

        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                displayed = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_to_main_button.check_clicked(pygame.mouse.get_pos()) == True:
                    Start_Screen()
                    displayed = False
                if play_level_again.check_clicked(pygame.mouse.get_pos()) == True:
                    Game_Screen(level)
                    displayed = False


        
        pygame.display.update()
        clock.tick(FRAME_RATE)

render.music.load('Audio/Time.mp3')
render.music.set_volume(render.music_volume)
render.music.play(-1)
Start_Screen()