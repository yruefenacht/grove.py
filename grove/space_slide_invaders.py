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
		

def main():
	run = True
	FPS = 60
	score = 0
	main_font = pygame.font.SysFont("comicsans", 50)
	
	player_vel = 5
	
	player = Entity(350, 600, PLAYER_SHIP)
	
	clock = pygame.time.Clock()
	
	client = None
	
	try:
		client = grove_client.GroveClient()
	except:
		print("Client connection could not be established")
	
	def redraw_window():
		WIN.blit(BG, (0, 0))
		
		score_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))
		WIN.blit(score_label, (10, 10))
		
		player.draw(WIN)
		
		pygame.display.update()
	
	while run:
		clock.tick(FPS)
		redraw_window()
		
		# Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		
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
				
main()

