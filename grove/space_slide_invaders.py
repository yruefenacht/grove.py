#!/bin/usr/env python

import pygame
import os
import time
import random
import grove_client

pygame.font.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Load assets
PLAYER_SHIP = pygame.image.load(os.path.join("grove", "assets", "space_player_ship.png"))
ENEMY_SHIP = pygame.image.load(os.path.join("grove", "assets", "space_enemy_ship.png"))
BG = pygame.transform.scale(pygame.image.load(os.path.join("grove", "assets", "space_bg.png")), (WIDTH,HEIGHT))

class Entity:
	def __init__(self, x, y, img):
		self.x = x
		self.y = y
		self.img = img
		self.mask = pygame.mask.from_surface(self.img)
		
	def draw(self, window):
		window.blit(self.img, (self.x, self.y))
		
	def get_width(self):
		return self.img.get_width()
	
	def get_height(self):
		return self.img.get_height()
		
	def collision(self, other_entity):
		return collide(self, other_entity)
		
def collide(entity1, entity2):
	offset_x = entity2.x - entity1.x
	offset_y = entity2.y - entity1.y
	return entity1.mask.overlap(entity2.mask, (offset_x, offset_y)) != None
	
def main():
	run = True
	FPS = 60
	score = 0
	main_font = pygame.font.SysFont("comicsans", 50)
	lost_font = pygame.font.SysFont("comicsans", 60)
	
	enemies = []
	enemies_vel = 3
	
	player_vel = 10
	
	player = Entity(350, 600, PLAYER_SHIP)
	
	clock = pygame.time.Clock()
	
	lost = False
	lost_count = 3
	
	client = None
	
	try:
		client_label = main_font.render("Connecting to client...", 1, (255, 255, 255))
		WIN.blit(client_label, (WIDTH/2 - client_label.get_width()/2, 425))
		pygame.display.update()
		client = grove_client.GroveClient()
	except:
		print("Client connection could not be established")
	
	def redraw_window():
		WIN.blit(BG, (0, 0))
		
		score_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))
		WIN.blit(score_label, (10, 10))
		
		for enemy in enemies:
			enemy.draw(WIN)
			
		player.draw(WIN)
		
		if lost:
			lost_label = lost_font.render("Game Over", 1, (255, 255, 255))
			WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
		
		pygame.display.update()
	
	counter = 0
	enemy_spawn_frequency = 100
	
	while run:
		clock.tick(FPS)
		redraw_window()
		
		if lost:
			lost_count += 1
			if lost_count > FPS * 3:
				run = False
			else:
				continue
		
		# Spawn Enemies
		if counter % enemy_spawn_frequency == 0:
			counter = 0
			if enemy_spawn_frequency > 1:
				enemy_spawn_frequency -= 1
			enemy = Entity(random.randrange(0, WIDTH-50), random.randrange(-1500, -100), ENEMY_SHIP)
			enemies.append(enemy)
			
		counter += 1
		
		# Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		
		# Movement keyboard
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and player.x - player_vel > 0:
			player.x -= player_vel
		if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:
			player.x += player_vel
			
		# Movement sensor
		if client is not None:
			distance = self.client.get_distance()
			player.x = distance
			
		# Movement enemies
		for enemy in enemies[:]:
			enemy.y += enemies_vel
			if player.collision(enemy):
				lost = True
			if enemy.y + enemy.get_height() > HEIGHT:
				score += 1
				enemies.remove(enemy)
			
def main_menu():
	title_font = pygame.font.SysFont("comicsans", 70)
	run = True
	while run:
		WIN.blit(BG, (0, 0))
		title_label = title_font.render("Press any key to begin...", 1, (255, 255, 255))
		WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
		pygame.display.update()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				main()	
	pygame.quit()
				
main_menu()

