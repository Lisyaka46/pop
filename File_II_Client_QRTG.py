class Error(): # Список ошибок или крашей в клиенте
	def error(self, error_number, register_problem = None):
		log_txt, i.number_pos_txt = i.mini_function('log'), '0'
		log = open('%s/log.log' % (self.dir_python_file), 'w')
		if error_number != '0g7503':
			self.audio_channel.play(self.MP3_Error)
		else:
			self.audio_channel.play(self.MP3_Crash)
		if error_number == '0g7500' or error_number == '0g7501':
			if error_number == '0g7500':
				print('%s Ошибка %s: Ваш никнейм сожержит запретный знак "%s"\n%s Повторите попытку' % (self.r_text_back_a, error_number, register_problem, self.r_text_back_a))
				log.write('%s\n%s [%s] Error %s: The nickname contains a forbidden sign "%s"' % (log_txt, self.r_text_back_a, asctime(), error_number, register_problem))
				i.number_pos_txt = '1'
			elif error_number == '0g7501':
				print('%s Ошибка %s: Ваш пароль сожержит запретный знак "/"\n%s Повторите попытку' % (self.r_text_back_a, error_number, self.r_text_back_a))
				log.write('%s\n%s [%s] Error %s: The password contains a forbidden sign "/"' % (log_txt, self.r_text_back_a, asctime(), error_number))
				i.number_pos_txt = '2'
			log.close()
			i.position = 'Register'
			i.register()
		elif error_number == '0g7502':
			print('%s Ошибка %s: Ваш "self.answer" не соответствует требованиям или содержит ошибку в "%s"' % (self.r_text_back_a, error_number, self.position))
			log.write('%s\n%s [%s] Error %s: your "self.answer" does not meet the requirements or contains an error in "%s"' % (log_txt, self.r_text_back_a, asctime(), error_number, self.position))
			log.close()
			if self.position.find('bank') != -1: self.ifip = 1
			if self.position == 'main_menu':
				if randint(0,4) == 2:
					i.animas(txt = '%s Если ты не знаешь некоторых комманд попробуй ввести: "help"' % (self.r_text_back_a))
				i.main_menu()
			elif self.position == 'coin_Q':
				print('%s Биржа' % (self.r_text_back_a))
				if self.active_coin_Q == False and self.active_coin_ruble == False: i.coin()
				else: i.coin_pr(True)
			elif self.position == 'console' or self.position == 'import_mode':
				if self.console_programm == 0: i.console_start()
				elif self.console_programm == 2:
					if randint(0,4) == 2:
						i.animas(txt = '%s Если ты не знаешь некоторых комманд попробуй ввести: "help"' % (self.r_text_back_a))
					i.main_menu()
			elif self.position == 'bank_b0': i.bank()
			elif self.position == 'bank_b1': i.buy_vaule()
			elif self.position == 'bank_b2': i.buy_sum_rel()
			elif self.position == 'game_play': i.gl_games()
			elif self.position == 'game':
				if randint(0,4) == 2:
					i.animas(txt = '%s Если ты не знаешь некоторых комманд попробуй ввести: "help"' % (self.r_text_back_a))
				i.main_menu()
			elif self.position == 'balanse_out': i.Balanse_out_account()
			elif self.position == 'rate': self.rate_update = 0, i.rate_pr()
			else: i.error('0g7503')
		else:
			if error_number == '0g7503':
				print('%s Неожидаймая ошибка %s: Краш системы///\n%s Выход из файла' % (self.r_text_back_a, error_number, self.r_text_back_a))
				log.write('%s\n%s [%s] Unexpected error %s: System CRACH///' % (log_txt, self.r_text_back_a, asctime(), error_number))
			elif error_number == '0g7504':
				print('%s Ошибка синтаксиса %s: Команда <%s> из ~мода некорректена\n%s %s, попробуй переустановить мод с этой командой' % (self.r_text_back_a, error_number, self.answer, self.r_text_back_a, self.name))
				log.write('%s\n%s [%s] Error syntax %s: The command <%s> from ~mod is incorrect' % (log_txt, self.r_text_back_a, asctime(), error_number, self.answer))
			elif error_number == '0g7506':
				print('%s Ошибка договора %s: Вакансия отменена из-за превышения цен' % (self.r_text_back_a, error_number))
				log.write('%s\n%s [%s] Contract error %s: The vacancy was canceled due to excess prices' % (log_txt, self.r_text_back_a, asctime(), error_number))
			elif error_number == '0g7507':
				print('%s Ошибка выполнения консольной программы меню %s: Команда оказалась системной - отказано в доступе...' % (self.r_text_back_a, error_number))
				log.write('%s\n%s [%s] Error executing the console menu program %s: The command turned out to be a system one - access was denied...' % (log_txt, self.r_text_back_a, asctime(), error_number))
			elif error_number == '0g7508':
				if self.ip_ass == 3:
					print('%s Ошибка импорта %s: Все моды уже за импортированы' % (self.r_text_back_a, error_number))
					log.write('%s\n%s [%s] Import error %s: the all mods been imported' % (log_txt, self.r_text_back_a, asctime(), error_number))
				else:
					print('%s Ошибка импорта %s: Мод "%s" уже был за импортирован' % (self.r_text_back_a, error_number, self.answer))
					log.write('%s\n%s [%s] Import error %s: the mod "%s" has already been imported' % (log_txt, self.r_text_back_a, asctime(), error_number, self.answer))
			elif error_number == '0g7509':
				print('%s Ошибка чтения файлов .viu %s: фаил "%s" не правильно записан или сохранён' % (self.r_text_back_a, error_number, self.answer))
				log.write('%s\n%s [%s] Error reading files .viu %s: file "%s" is not correctly written or saved' % (log_txt, self.r_text_back_a, asctime(), error_number, self.answer))
			log.close()
			i.position = 'ERROR'
			if error_number == '0g7506': i.bank()
			elif error_number == '0g7508':
				if self.console_programm == 0: i.console_start()
				elif self.console_programm == 2: i.main_menu()
				else: i.error('0g7503')
			elif error_number == '0g7503':
				self.audio_channel.play(self.MP3_Crash)
				if self.chill_change_return == 1: self.chill_change.kill()
				sleep(1.1)
				sys.exit(0)
	pass
class Console(Error): # Класс консоли в клиенте
	def console_start(self): # Начало работы консоли
		i.position = 'console'
		self.ipp = None
		if i.console_programm == 0:
			i.animas(n = 1, txt = 'Консольная строка:')
			self.answer = input('Консольная строка: ')
			i.iF_console()
		elif i.console_programm == 2:
			print('%s Отказано в доступе' % (self.r_text_back_a))
			self.audio_channel.play(self.MP3_Denial)
			i.main_menu()
		else:
			i.error('0g7503')
	def iF_console(self): # Проверка команды для консоли
		if len(self.answer) == 0 and self.console_programm != 4: i.console_start()
		elif self.answer == '/clear' or self.answer == '/cls' or self.answer == '/clear_console':
			if self.console_programm == 2: i.mini_function('menu_console')
			if self.console_programm != 4:
				i.clear_console()
				print('%s Произведена очистка!' % (self.r_text_back_a))
				self.audio_channel.play(self.MP3_Complete)
			else:
				print('%s Команда "%s" отвечает за очистку консоли (через Консольную строку)' % (self.r_text_back_a, self.answer))
				return True
			i.mini_function('console_end_command')
		elif self.answer == '<' or\
		self.answer == 'exit' or\
		self.answer == '/q':
			if self.console_programm == 2:
				i.mini_function('menu_console')
				i.error('0g7507')
			if self.console_programm != 4:
				i.main_menu()
			else:
				print('%s Команда "%s" отвечает за выход из консоли (через Консольную строку)' % (self.r_text_back_a, self.answer))
				return True
		elif self.answer == '/mode':
			if self.console_programm == 2:
				i.mini_function('menu_console')
			if self.console_programm != 4:
				if self.console_mode_activate == False:
					self.console_mode_activate = True
					i.read_modepacks()
				else:
					print('%s Вы уже обновили библиотеку модов' % (self.r_text_back_a))
					i.mini_function('console_end_command')
			else:
				print('%s Команда "%s" отвечает за обновление библиотеки модов (через Консольную строку)' % (self.r_text_back_a, self.answer))
				return True
		elif self.answer == '/log read' or self.answer == '/log_read':
			if self.console_programm == 2: i.mini_function('menu_console')
			if self.console_programm != 4: i.log_file_change('log_read')
			else:
				print('%s Команда "%s" отвечает за прочтение файла log.log (через Консольную строку)' % (self.r_text_back_a, self.answer))
				return True
		elif self.answer == '/log note' or self.answer == '/log_note' or self.answer == '/note':
			if self.console_programm == 2: i.mini_function('menu_console')
			if self.console_programm != 4: i.log_file_change('note')
			else:
				print('%s Команда "%s" отвечает за создание в файле log.log заметки (через Консольную строку)' % (self.r_text_back_a, self.answer))
				return True
		elif self.answer == '/log clear' or self.answer == '/log_clear':
			if self.console_programm == 2: i.mini_function('menu_console')
			if self.console_programm != 4: i.log_file_change('log_clear')
			else:
				print('%s Команда "%s" отвечает за очистку файла log.log (через Консольную строку)' % (self.r_text_back_a, self.answer))
				return True
		elif self.answer == '/import' or self.answer == '/imp':
			if self.console_programm == 2: i.mini_function('menu_console')
			if self.console_programm != 4:
				if self.console_mode_activate == True:
					self.position = 'import_mode'
					i.console_mode()
				else:
					self.position = 'import_mode'
					i.animas(txt = '%s %s, вы ещё не обновили пакет модов' % (self.r_text_back_a, self.name))
					i.animas(txt = '%s Команда: /mode' % (self.r_text_back_a))
			else:
				print('%s Команда "%s" отвечает за импорт модов, доступно после обновления библ. модов (через Консольную строку)' % (self.r_text_back_a, self.answer))
				return True
			i.mini_function('console_end_command')
		else:
			if self.console_programm == 0 or self.console_programm == 4:
				i.mode_command_check()
			else:
				i.error('0g7502')
	def console_mode(self):
		self.position, self.x = 'import_mode', 0
		self.answer = input('Введите команду импорта или мод который вы хотите импортировать: ')
		i.import_console_mode()
	def import_console_mode(self): # Импортирование модов или ветвь команд импорта в консоли
		if self.answer == '<' or self.answer == '-' or self.answer == 'exit':
			print('%s Выход из Импорта модов...' % (self.r_text_back_a))
			i.mini_function('console_end_command')
		elif self.answer.find == 'all':
			if len(self.ModeFic_global[11]) == 0 or self.indif == 'complete':
				self.indif = 'all'
				if self.developer_mode == True:
					print('import mods all!')
				if len(self.ModeFic_global[0]) > 0:
					for self.x in range(len(self.ModeFic_global[0])):
						self.answer = self.ModeFic_global[0][self.x]
						if self.developer_mode == True:
							print('self.x: <%s>\nlen(self.ModeFic_global[0]): <%s>' % (self.x, len(self.ModeFic_global[0])))
						i.pr_answer_mode()
			elif len(self.ModeFic_global[11]) < len(self.ModeFic_global[0]):
				self.pos_txt_system = 0
				self.global_command_number_system = -1
				print('%s Очистка импортированных модов...' % (self.r_text_back_a))
				i.ModeFic_clear(9), i.ModeFic_clear(10)
				if self.developer_mode == True:
					print('+')
				self.indif = 'complete'
				i.import_console_mode()
			elif len(self.ModeFic_global[11]) == len(self.ModeFic_global[0]):
				print('%s %s, вы уже проимпортировали все установленные моды' % (self.r_text_back_a, self.pol_name))
				self.ip_ass = 3
				i.error('0g7508')
		elif self.answer == 'delete':
			i.ModeFic_clear(9), i.ModeFic_clear(13)
			self.pos_txt_system = 0
			print('%s Все моды успешно удалены из %s\n%s Вы можете их повторно загрузить: /mode' % (self.r_text_back_a, self.r_text_back_b, self.r_text_back_a))
			i.mini_function('console_end_command')
		elif self.answer == 'info':
			symbol = ''
			if len(self.ModeFic_global[0]) > 1: symbol = 'ы'
			if len(self.ModeFic_global[0]) != 0:
				print('...Мод%s: ' % (symbol), end='')
				for x in self.ModeFic_global[0]:
					if self.ModeFic_global[0].index(x) != len(self.ModeFic_global[0])-1: print(x, end=', ')
					else: print(x)
			else: print('%s Никаких модов не установлено!' % (self.r_text_back_a))
			i.console_mode()
		elif len(self.ModeFic_global[0]) > self.x:
			if len(self.ModeFic_global[0]) > 0:
				for self.x in range(0, len(self.ModeFic_global[0])):
					if self.developer_mode == True:
						print('\rAnswer: <%s> | Mode: <%s>' % (self.answer, self.ModeFic_global[0][self.x]),end=' '*30)
					if len(self.ModeFic_global[0]) > self.x:
						if self.answer == self.ModeFic_global[0][self.x]: break
				if self.answer == self.ModeFic_global[0][self.x]:
					self.indif, self.logic_control[0] = 'Nall', 'False'
					i.read_mode_importing()
				else: i.error('0g7502')
			else: i.error('0g7502')
	def pr_answer_mode(self): # Проверка названия мода для импорта
		if self.developer_mode == True:
			print('self.x: ', self.x)
			print('importing mode: ', len(self.ModeFic_global[11]))
		if self.x < len(self.ModeFic_global[0]):
			if self.answer == self.ModeFic_global[0][self.x]:
				if len(self.ModeFic_global[11]) != 0 and self.indif != 'all':
					for self.x in range(0, len(self.ModeFic_global[11])):
						if self.answer == self.ModeFic_global[11][self.x] and len(self.ModeFic_global[11]) < len(self.ModeFic_global[0]):
							print('%s Вы уже импортировали мод "%s"' % (self.r_text_back_a, self.answer))
						elif len(self.ModeFic_global[11]) == len(self.ModeFic_global[0]):
							print('%s %s, вы уже проимпортировали все установленные моды' % (self.r_text_back_a, self.pol_name))
							self.ip_ass = 3
						i.error('0g7508')
						self.import_act = False
					if self.import_act == True:
						self.logic_control[0] = 'False'
						i.read_mode_importing()
				else:
					self.import_act = True
					self.logic_control[0] = 'False'
					i.read_mode_importing()
	def read_mode_importing(self): # Импорт мода или модов
		if self.developer_mode == True:
			print(self.console_programm)
			print(self.indif)
			print(self.ipp)
			print('logic_control[0]: ', self.logic_control[0])
		if self.logic_control[0] == 'False':
			self.ModeFic_global[11].append(self.ModeFic_global[0][self.x])
			self.mode, self.read_mode_import = open('%s/ModePack/%s' % (self.dir_python_file, self.ModeFic_global[0][self.x])), self.ModeFic_global[0][self.x]
			self.txt, self.txting, self.number_pos, self.visual_end_reading_modes, self.ip_ass, incident, sleep_command = None, '', 0, False, 1, 0, 0
			mode_all_symbol = self.mode.read()
			self.cv_file_full = len(mode_all_symbol)
			self.mode.seek(0)
			self.audio_channel.play(self.MP3_Warning)
			if self.indif == 'all': i.animas(txt = '%s Подождите идёт импорт всех модов...' % (self.r_text_back_a))
			else: i.animas(txt = '%s Подождите идёт импорт мода "%s"...' % (self.r_text_back_a, self.answer))
			while self.txt != '!':
				self.txt = self.mode.read(1)
				if self.developer_mode == True:
					i.mini_function('developer_import_info')
				if self.txt == '=':
					self.txting_check, self.txting = self.txting, ''
				elif self.txt == '{' and self.txting_check == 'com':
					if self.developer_mode == True:
						print('Проверка совпадения команды с системными!')
					self.command_txting, self.txting_check = False, None
					for y in self.all_commands:
						for y1 in y:
							if self.txting == y1:
								symbol = '=='
								self.command_txting = True
								break
							else:
								symbol = '!='
							if self.developer_mode == True:
								print(' '*30, end = '')
								print('\rКоманда: "%s" %s "%s"  ' % (self.txting, symbol, y1), end = '')
								sleep(0.4)
						if self.command_txting == True:
							break
					if self.developer_mode == True:
						print()
					if self.command_txting == False:
						self.ModeFic_global[1].append(self.txting)
						self.global_command_number_system += 1
						self.import_command, self.txting = self.txting, ''
						if self.developer_mode == True:
							i.mini_function('developer_import_info')
						while self.txt != '}':
							self.txt = self.mode.read(1)
							if self.developer_mode == True:
								i.mini_function('developer_import_info')
							if self.txt == '@' and self.txting != 'var':
								self.ModeFic_global[6].append('main_menu')
								if self.developer_mode == True:
									print('command_radar = main_menu')
								self.txting = ''
							elif self.txt == '(':
								self.number_pos += 1
								self.ModeFic_global[2].append(self.txting)
								self.txting = ''
								if self.ModeFic_global[2][len(self.ModeFic_global[2])-1] == 'print':
									while self.txt != ';':
										self.txt = self.mode.read(1)
										if self.developer_mode == True:
											i.mini_function('developer_import_info')
										if self.txt == ')':
											self.ModeFic_global[3].append(self.txting)
											self.txting = ''
										if self.txt == '[':
											if self.txting != '':
												self.txting2 = self.txting
												self.txting = ''
											while self.txt != ']':
												self.txt = self.mode.read(1)
												if self.developer_mode == True:
													i.mini_function('developer_import_info')
												if self.txt == '/' or self.txt == ']':
													if self.txt != ']':
														self.txt = self.mode.read(1)
														if self.developer_mode == True:
															i.mini_function('developer_import_info')
													if self.txting3 == '': self.txting3 = 0
													if self.txting != '':
														if self.txting.isdigit() != True:
															for y in range(len(self.ModeFic_global[7])):
																if self.developer_mode == True:
																	print('len(self.ModeFic_global[7]: <%s>' % (len(self.ModeFic_global[7])))
																	print('self.ModeFic_global[7]: <%s>' % (self.ModeFic_global[7]))
																	print('self.ModeFic_global[7][y]: <%s>' % (self.ModeFic_global[7][y]))
																	print('str(self.txting) == self.ModeFic_global[7][y]: <%s>' % (str(self.txting) == self.ModeFic_global[7][y]))
																	i.mini_function('developer_import_info')
																if self.txting == self.ModeFic_global[7][y]:
																	self.txting = int(self.ModeFic_global[8][y])
																	break
														else:
															self.txting = int(self.txting)
														if self.txting3 != 0:
															if element == '+': self.txting3 += self.txting
															elif element == '-': self.txting3 -= self.txting
															elif element == '*': self.txting3 *= self.txting
															elif element == '/': self.txting3 /= self.txting
															elif element == '\\': self.txting3 //= self.txting
															elif element == '%': self.txting3 %= self.txting
															elif element == '$': self.txting3 **= self.txting
														else:
															self.txting3 = self.txting
														element = self.txt
														self.txting = ''
														if self.txt == ']':
															self.txting += self.txting2 + str(self.txting3)
															self.txting2, self.txting3 = '', ''
												else:
													if self.txt != ';' and\
													self.txt != ']' and\
													self.txt != ')' and\
													self.txt != '\n' and\
													self.txt != '\t':
														self.txting += self.txt
												i.print_importing()
										else:
											if self.txt != ';' and\
											self.txt != ']' and\
											self.txt != ')' and\
											self.txt != '\n' and\
											self.txt != '\t':
												self.txting += self.txt
										i.print_importing()
								elif self.txting == 'sleep':
									while self.txt != ')':
										self.txt = self.mode.read(1)
										if self.developer_mode == True:
											i.mini_function('developer_import_info')
										if self.txt == ')':
											if self.txting.isnumeric() == True:
												if int(self.txting) == 0:
													self.ModeFic_global[3].append('0.01')
													self.txting2 = '0.01'
												elif int(self.txting) < 0:
													self.ModeFic_global[3].append(str(abs(self.txting)))
													self.txting2 = str(abs(self.txting))
												elif int(self.txting) > 0:
													self.ModeFic_global[3].append(str(self.txting))
													self.txting2 = self.txting
												self.txting = ''
												sleep_command = 1
											else:
												i.error('0g7504')
										else:
											if self.txt != ')' and\
											self.txt != ' ' and\
											self.txt != '\n' and\
											self.txt != '\t':
												self.txting += self.txt
										i.print_importing()
									while self.txt != ';':
										self.txt = self.mode.read(1)
										if self.developer_mode == True:
											i.mini_function('developer_import_info')
										if self.txt == '~':
											if int(self.txting2) >= 3:
												self.ModeFic_global[9].append('True')
												self.txting2 = ''
												self.ipp += 2
												if self.developer_mode == True:
													print('!ipp = %s' % (self.ipp))
										elif self.txt == ';':
											if self.txting2 != None:
												self.txting2 = ''
											if self.developer_mode == True:
												print('~!~')
											if int(self.txting) > 0:
												self.ModeFic_global[9].append('True')
											else:
												self.ModeFic_global[9].append('False')
											self.txting = ''
										else:
											if self.txt != ')' and\
											self.txt != ' ' and\
											self.txt != ';' and\
											self.txt != '\n' and\
											self.txt != '\t':
												self.txting += self.txt
										i.print_importing()
							elif self.txt == '[':
								self.number_pos += 1
								self.ModeFic_global[2].append(self.txting)
								self.txting = ''
								while self.txt != ';':
									self.txt = self.mode.read(1)
									if self.developer_mode == True:
										i.mini_function('developer_import_info')
									if self.txt == ']':
										if incident == 0:
											self.ModeFic_global[3].append(self.txting)
										else:
											self.ModeFic_global[10].append(self.txting)
											incident = 0
										self.txting = ''
									elif self.txt == ',' and self.txting == '__text__':
										incident = 1
										i.log_run('__text__')
									else:
										if self.txt != ';' and\
										self.txt != '\n' and\
										self.txt != '\t':
											self.txting += self.txt
									i.print_importing()
							elif self.txt == '$':
								self.txt, self.txting = None, ''
								while self.txt != '$':
									self.txt = self.mode.read(1)
									if self.developer_mode == True:
										i.mini_function('developer_import_info')
									if self.txt == '$':
										if self.txting == 'con_st': self.ModeFic_global[6].append('console')
										elif self.txting == 'main_menu': self.ModeFic_global[6].append('main_menu')
										elif self.txting == 'coin': self.ModeFic_global[6].append('coin_Q')
										elif self.txting == 'b1': self.ModeFic_global[6].append('bank_b0')
										elif self.txting == 'b2': self.ModeFic_global[6].append('bank_b1')
										elif self.txting == 'b3': self.ModeFic_global[6].append('bank_b2')
										else:
											i.error('0g7504')
										if self.developer_mode == True:
											print('command_radar = <%s>' % (self.ModeFic_global[6][len(self.ModeFic_global[6]) - 1]))
										self.txting = ''
									else:
										if self.txt != '\n' and\
										self.txt != '\t':
											self.txting += self.txt
									i.print_importing()
							elif self.txt == '@' and self.txting == 'var':
								self.txting = ''
								if self.developer_mode == True:
									print('Считываем имя переменной!')
								while self.txt != '=':
									self.txt = self.mode.read(1)
									if self.developer_mode == True:
										i.mini_function('developer_import_info')
									if self.txt == '=':
										self.ModeFic_global[7].append(self.txting)
										self.txting = ''
									else:
										if self.txt != '\n' and\
										self.txt != '\t' and\
										self.txt != ' ':
											self.txting += self.txt
									i.print_importing()
								if self.developer_mode == True:
									print('Считываем значение переменной!')
								while self.txt != '?':
									self.txt = self.mode.read(1)
									if self.developer_mode == True:
										i.mini_function('developer_import_info')
									if self.txt == '?':
										self.ModeFic_global[8].append(self.txting)
										self.txting = ''
									else:
										if self.txt != '\n' and\
										self.txt != '\t' and\
										self.txt != ' ':
											self.txting += self.txt
									i.print_importing()
							elif self.txt == '%':
								if self.txting == 'expl':
									self.txting, self.txt = '', None
									self.txt = self.mode.read(1)
									if self.developer_mode == True:
										i.mini_function('developer_import_info')
									if self.txt == '(':
										while self.txt != ')':
											self.txt = self.mode.read(1)
											if self.developer_mode == True:
												i.mini_function('developer_import_info')
											if self.txt == ')':
												if self.len_ModeFic_expl == 0:
													expl_indification = len(self.ModeFic_global[12])
													self.ModeFic_global[12].append(self.txting)
													self.len_ModeFic_expl = 1
												elif self.len_ModeFic_expl == 1:
													self.ModeFic_global[12][expl_indification] = self.txting
												self.txting = ''
											else:
												if self.txt != '\n' and\
												self.txt != '\t':
													self.txting += self.txt
									elif self.txt == '{':
										while self.txt != '}':
											self.txt = self.mode.read(1)
											if self.developer_mode == True:
												i.mini_function('developer_import_info')
											if self.txt == '}':
												if self.txting == '__info__': self.txting = 'Обычный вывод текста в консоль'
												elif self.txting == '__def__': self.txting = 'Выполение функции перехода'
												elif self.txting == '__on__': self.txting = 'Включение чего-либо'
												elif self.txting == '__off__': self.txting = 'Выключение чего-либо'
												else: self.txting = '0'
												if self.len_ModeFic_expl == 0:
													self.expl_indification, self.len_ModeFic_expl = len(self.ModeFic_global[12]), 1
													self.ModeFic_global[12].append(self.txting)
												elif self.len_ModeFic_expl == 1:
													self.ModeFic_global[12][self.expl_indification] = self.txting
												self.txting = ''
											else:
												if self.txt != '\n' and\
												self.txt != '\t':
													self.txting += self.txt
											i.print_importing()
							else:
								if self.txt != '\n' and\
								self.txt != '\t':
									self.txting += self.txt
							i.print_importing()
						if self.len_ModeFic_expl == 0:
							self.ModeFic_global[12].append('0')
						self.txt, self.txting, self.x = None, '', None
					else:
						print('\n%s Команда "%s" <self.ModeFic_global> совпадает с системной командой в моде "%s"\n%s Остановка и очистка импорта' % (self.r_text_back_a, self.txting, self.read_mode_import, self.r_text_back_a))
						i.ModeFic_clear(self.ipp)
						i.error('0g7504')
						i.mini_function('console_end_command')
				elif self.txt == '/':
					self.number_pos += 1
					self.ModeFic_global[4].append(self.number_pos)
					self.ModeFic_global[5].append(self.pos_txt_system)
					self.pos_txt_system += self.number_pos
					self.number_pos = 0
					self.ModeFic_global[2].append('cl')
					if sleep_command == 0:
						self.ModeFic_global[9].append('-')
					else:
						sleep_command = 0
					while self.txt != '?':
						self.txt = self.mode.read(1)
						if self.developer_mode == True:
							i.mini_function('developer_import_info')
						if self.txt == '?':
							self.ModeFic_global[3].append(self.txting)
							self.txting = ''
						else:
							if self.txt != '?':
								self.txting += self.txt
						i.print_importing()
				else:
					if self.txt != '=' and\
					self.txt != '\n' and\
					self.txt != '\t' and\
					self.txt != '{':
						self.txting += self.txt
				i.print_importing()
			if self.developer_mode == True:
				print('Break, close mode')
			self.logic_control[0] = 'End'
			self.mode.close()
			self.cv_file_full = 0
			self.visual_end_reading_modes = False
			if self.developer_mode == True:
				print('logic_control[0]: ',self.logic_control[0])
				print(self.logic_control[0] == 'End')
		if self.logic_control[0] == 'End':
			print('\n%s Импорт модов прошёл успешно!\nТеперь вам доступны команды:' % (self.r_text_back_a))
			if len(self.ModeFic_global[1]) != 0:
				for y in range(len(self.ModeFic_global[1])):
					print('  %s. %s' % (y + 1, self.ModeFic_global[1][y]))
			if self.developer_mode == True:
				print(self.ModeFic_global[0], 'Имя загруженных модов')
				print(self.ModeFic_global[1], 'Имя команд')
				print(self.ModeFic_global[2], 'Название действий в команде')
				print(self.ModeFic_global[3], 'Итог действий в команде')
				print(self.ModeFic_global[4], 'Кол-во действий в команде')
				print(self.ModeFic_global[5], 'Начало отсчёта действий в команде')
				print(self.ModeFic_global[6], 'Место выполнения команды')
				print(self.ModeFic_global[7], 'Имя переменных')
				print(self.ModeFic_global[8], 'Значения переменных')
				print(self.ModeFic_global[9], 'Итог вывода сообщения о спящем режиме')
				print(self.ModeFic_global[10], 'Записываемый текст в log.log')
				print(self.ModeFic_global[11], 'Имя импортированных модов')
				print(self.ModeFic_global[12], 'Поянение команд из модов')
			self.audio_channel.play(self.MP3_Open)
			i.mini_function('console_end_command')
		else:
			i.error('0g7503')
	def print_importing(self):
		if self.developer_mode == False:
			self.printing_import_text = round(self.mode.tell() / (self.cv_file_full/100))
			self.stoping = randint(1, 10)
			self.sdi = self.stoping/5
			if self.mode.tell() >= self.cv_file_full:
				self.visual_end_reading_modes = True
				print('\r%s: [100' % (self.read_mode_import) + R'%' + '/100' + R'%' + ']_%s/%s_(-- sdi)'\
				% (self.cv_file_full, self.cv_file_full), end = '                                     ')
			else:
				if self.visual_end_reading_modes == False:
					print('\r%s: [%s' % (self.read_mode_import, self.printing_import_text) + R'%' + '/100' + R'%' + ']_%s/%s_(%s sdi)                                   '\
					% (self.mode.tell(), self.cv_file_full, round(100/(self.sdi*5))), end = '  ')
			self.printing_import_text = None
			sleep(self.sdi - (self.sdi / 2))
	pass
class Brower(Error):
	def brower_start(self):
		sleep(0.1)
		i.animas(loading = True, txt = '%s Загрузка браузера' % (self.r_text_back_a))
		if self.developer_mode == True:
			print(self.internet_start_str)
		i.brower_main_menu()
	def animas(self, loading = False, n = 0, txt = None):
		if loading != False and loading != True: loading = False
		if n != 0 and n != 1: n = 0
		for self.x in str(txt):
			sleep(0.04)
			self.print_text_global += self.x
			if keyboard.is_pressed('Alt') != True:
				print('\r%s' % (self.print_text_global), end='')
			else:
				while keyboard.is_pressed('Alt') != False: pass
				print('\r%s' % (txt), end='')
				break
		if loading == True:
			self.stoping = randint(1, 10)
			self.sdi = self.stoping/5
			for self.att in range(0, round(self.sdi*8)):
				for y1 in range(0,3):
					print('\r%s ' % (txt), end = self.loading_sym[y1] + ' ')
					sleep(0.08)
			print('\r%s ' % (txt), end = '√ ')
		sleep(0.2)
		if n == 0: print('')
		elif n == 1: print('\r', end = '')
		self.print_text_global = ''
	def brower_main_menu(self):
		if self.internet_start_str == 'newstap':
			i.animas(n = 1, txt = '%s Главная:' % (self.r_text_back_a))
			self.answer = input('%s Главная: ' % (self.r_text_back_a))
			i.iF_brower('menu')
		else:
			self.internet_link = self.internet_start_str
			i.brower_output()
	def iF_brower(self, br_position):
		if br_position == 'menu':
			if self.answer == 'Ввод' or self.answer == 'Поиск' or self.answer == 'search' or self.answer == 'поиск':
				self.file = open('%s/Internet QRTG/Search.javas' % (self.dir_python_file))
				self.txt, self.txting = None, ''
				while True:
					self.txt = self.file.read(1)
					if self.txt == '{':
						if self.txting == 'search':
							self.txting = ''
							self.file.read(1)
							while self.txt != '}':
								self.txt = self.file.read(1)
								if self.txt == '\n':
									self.internet_searching_list.append(self.txting)
									self.txting = ''
								else:
									if self.txt != '{' and\
									self.txt != '\t' and\
									self.txt != '\n' and\
									self.txt != '}':
										self.txting += self.txt
							break
					else:
						if self.txt != '{' and\
						self.txt != '\t' and\
						self.txt != '\n' and\
						self.txt != '}':
							self.txting += self.txt
				if len(self.internet_searching_list) != 0:
					self.internet_text_input = '%s Последние поиски: ' % (self.r_text_back_a)
					for self.x in range(0, len(self.internet_searching_list)):
						if self.x != len(self.internet_searching_list) - 1:
							self.internet_text_input += '%s, ' % (self.internet_searching_list[self.x])
						else:
							self.internet_text_input += '%s. ' % (self.internet_searching_list[self.x])
					i.animas()
				i.brower_search()
			elif self.answer == '<' or self.answer == 'exit' or self.answer == 'выход' or self.answer == 'выйти':
				i.animas(n = 1, txt = '%s Вы действительно хотите выйти из браузера?:' % (self.r_text_back_a))
				self.answer = input('%s Вы действительно хотите выйти из браузера?: ' % (self.r_text_back_a))
				if self.answer == 'Yes' or self.answer == 'yes'\
				or self.answer == 'Y' or self.answer == 'y'\
				or self.answer == 'Да' or self.answer == 'да':
					i.animas(loading = True, txt = '%s Выход из браузера' % (self.r_text_back_a))
					i.main_menu()
				elif self.answer == 'No' or self.answer == 'no'\
				or self.answer == 'N' or self.answer == 'n'\
				or self.answer == 'Нет' or self.answer == 'нет':
					i.animas(txt = '%s Хорошо...' % (self.r_text_back_a))
					i.animas(loading = True, txt = '%s Продолжаем работу' % (self.r_text_back_a))
					i.brower_main_menu()
			elif self.answer == '+':
				self.internet_start_str = 'newstap'
				if self.save_data_all == True:
					i.saving_data('ALL')
				i.animas(txt = '%s "Главная страница" - успешно добавлена на начальный запуск' % (self.r_text_back_a))
				i.brower_main_menu()
			elif self.answer == 'information' or self.answer == '?' or self.answer == 'Информация' or self.answer == 'информация':
				list_info = ['%s Информация браузера QRTG:' % (self.r_text_back_a),\
				'___ 1. Все ссылки пишутся после знака "/" как агрумента',\
				'___ 2. Поиски по браузеру осуществляются по аргументу "*satt" как ссылки по умолчанию',\
				'___ 3. Если поиск оказался неизвестным то скорее всего "satt/<ваш запрос>" как ссылка была введена неверно',\
				'___ 4. Ложные поиски можно открыть в обычном браузере по возможности...']
				for self.x in list_info:
					i.animas(txt = self.x)
				i.brower_search()
			else:
				i.animas(txt = '%s Что-то пошло не так, %s попробуй ввести другую команду...' % (self.r_text_back_a, self.name))
				i.brower_main_menu()
		elif br_position == 'search':
			if self.internet_searching == None:
				self.internet_searching = self.answer + '\n'
			else:
				self.internet_searching += self.answer + '\n'
			for self.x in range(0, len(self.internet_searching_list)):
				if self.internet_searching == None:
					self.internet_searching = self.internet_searching_list[self.x] + '\n'
				else:
					self.internet_searching += self.internet_searching_list[self.x] + '\n'
			if self.save_data_all == True:
				i.saving_data('ALL')
			if self.answer == 'information' or self.answer == '?' or self.answer == 'Информация' or self.answer == 'информация':
				list_info = ['%s Поиски браузера QRTG:' % (self.r_text_back_a),\
				'1. Предсказатель - Предсказывает по твоим словам!',\
				'2. Погода - Какая погода у нас сегодня?']
				for self.x in list_info:
					i.animas(txt = self.x)
				i.brower_search()
			elif self.answer == '<' or self.answer == 'exit' or self.answer == 'выход' or self.answer == 'выйти':
				i.animas(loading = True, txt = '%s Переход на главную страницу' % (self.r_text_back_a))
				self.internet_start_str = 'newstap'
				i.brower_main_menu()
			else:
				i.brower_search_arg(self.internet_protocol)
				if i.brower_search_arg(self.internet_protocol) == False:
					i.animas(txt = '%s Похоже %s, вы ввели неправельную ссылку или я не понял запрос...' % (self.r_text_back_a, self.name))
					i.brower_search()
				else:
					i.brower_output()
		elif br_position == 'satt':
			if self.answer == '+':
				return '+'
			elif self.answer == '<' or self.answer == 'exit' or self.answer == 'выход' or self.answer == 'выйти':
				return '<'
	def brower_search(self):
		i.animas(n = 1, txt = '%s Поиск по браузеру QRTG:' % (self.r_text_back_a))
		self.answer = input('%s Поиск по браузеру QRTG: ' % (self.r_text_back_a))
		i.iF_brower('search')
	def brower_search_arg(self, protocol):
		if protocol == 'satt':
			if self.answer == 'Предсказатель' or self.answer == 'предсказатель' or self.answer.find('редсказатель') != -1 or\
			self.answer == 'the predictor' or self.answer == 'The predictor' or self.answer.find('predictor') != -1 or self.answer == 'Predictor':
				self.internet_link = 'satt/randomprint'
				i.brower_output()
			elif self.answer == 'weather' or self.answer == 'Weather' or self.answer == 'погода' or self.answer == 'Погода':
				self.internet_link = 'satt/weather'
				i.brower_output()
			else:
				return False
	def brower_distributor(self):
		if self.internet_link.find('satt') != -1:
			if self.internet_link.find('randomprint') != -1:
				return 'randomprint'
			elif self.internet_link.find('weather') != -1:
				return 'randomweather'
	def brower_output(self):
		if i.brower_distributor() == 'randomprint':
			i.animas(n = 1, txt = '%s Предсказатель:' % (self.r_text_back_a))
			self.answer = input('%s Предсказатель: ' % (self.r_text_back_a))
			if i.iF_brower('satt') == '+':
				self.internet_start_str = 'satt/randomprint'
				if self.save_data_all == True:
					i.saving_data('ALL')
				i.animas(txt = '%s "Страница Предсказатель" - успешно добавлена на начальный запуск' % (self.r_text_back_a))
				i.brower_output()
			elif i.iF_brower('satt') == '<':
				i.animas(loading = True, txt = '%s Выход на поисковую строку' % (self.r_text_back_a))
				i.brower_search()
			else:
				i.animas(loading = True, txt = '%s Гадаю...' % (self.r_text_back_a))
				self.att = randint(0, 9)
				if self.answer.find('?') == -1:
					list_info = [\
					'%s Не говорите сегодня слово/имя "%s"... ' % (self.r_text_back_a, self.answer),\
					'%s Вам надо поспать, "%s" плохо на вас влияет... ' % (self.r_text_back_a, self.answer),\
					'%s "%s" это отличный вариант по моему мнению) ' % (self.r_text_back_a, self.answer),\
					'%s Я не думаю что "%s" вам сегодня пригодится ' % (self.r_text_back_a, self.answer),\
					'%s "%s" это укромное место..) ' % (self.r_text_back_a, self.answer),\
					'%s Плохая идея - "%s" фу... ' % (self.r_text_back_a, self.answer),\
					'%s Что-то в "%s" всё-таки есть такого, загадочного) ' % (self.r_text_back_a, self.answer),\
					'%s Вам надо поесть, съеште "%s") ' % (self.r_text_back_a, self.answer),\
					'%s В "%s" находится то что вам сейчас нужно ' % (self.r_text_back_a, self.answer),\
					'%s О боже! не берите "%s" - ну я конечно в шутку) ' % (self.r_text_back_a, self.answer)\
					]
				elif self.answer.find('?') != -1:
					list_info = [\
					'%s Думаю что да ' % (self.r_text_back_a),\
					'%s Неее, точно нет... ' % (self.r_text_back_a),\
					'%s Если вы сами не против то да, конечно) ' % (self.r_text_back_a),\
					'%s Нет ' % (self.r_text_back_a),\
					'%s Да ' % (self.r_text_back_a),\
					'%s Возможно) ' % (self.r_text_back_a),\
					'%s Скорее нет чем да ' % (self.r_text_back_a),\
					'%s Скорее да чем нет ' % (self.r_text_back_a),\
					'%s Я не знаю... ' % (self.r_text_back_a),\
					'%s Ок ' % (self.r_text_back_a)\
					]
				i.animas(txt = list_info[self.att])
				i.brower_output()
		if i.brower_distributor() == 'randomweather':
			i.animas(loading = True, txt = '%s Прогноз погоды от %s' % (self.r_text_back_a, self.r_text_back_b))
			i.animas(n = 1, txt = '%s %s, Обновите прогноз:' % (self.r_text_back_a, self.name))
			self.answer = input('%s %s, Обновите прогноз: ' % (self.r_text_back_a, self.name))
			if self.answer == 'update' or self.answer == 'Update' or self.answer == 'Обновить' or self.answer == 'обновить':
				i.animas(loading = True, txt = '%s Подождите немного)' % (self.r_text_back_a))
				self.att = randint(0, 4)
				self.gl_time = localtime()
				if self.gl_time[3] < 22 and self.gl_time[3] > 7:
					list_info = [\
					'%s %s, Похоже я не смог определить вашу погоду...' % (self.r_text_back_a, self.name),\
					'%s По моим данным сегодня возможно выглянет солнышко)' % (self.r_text_back_a),\
					'%s Как жалко что у вас, %s, так пасмурно сегодня' % (self.r_text_back_a, self.name),\
					'%s Похоже.. %s, погода сегодня непослушная...' % (self.r_text_back_a, self.name),\
					'%s Та самая погода, в которой можно пойти прогуляться)' % (self.r_text_back_a)\
					]
				else:
					list_info = [\
					'%s %s, Как-то на улице темновато, но ясно)' % (self.r_text_back_a, self.name),\
					'%s Дождик... Под него очень хорошо засыпается' % (self.r_text_back_a),\
					'%s %s, Похоже я не смог определить вашу погоду...' % (self.r_text_back_a, self.name),\
					'%s %s, Там как-то ветренно, вам не кажется?' % (self.r_text_back_a, self.name),\
					'%s Было солнце, теперь луна с облачками гуляет' % (self.r_text_back_a)\
					]
				i.animas(txt = list_info[self.att])
				i.brower_output()
			elif i.iF_brower('satt') == '+':
				self.internet_start_str = 'satt/weather'
				if self.save_data_all == True:
					i.saving_data('ALL')
				i.animas(txt = '%s "Страница Прогноз погоды" - успешно добавлена на начальный запуск' % (self.r_text_back_a))
				i.brower_output()
			elif i.iF_brower('satt') == '<':
				i.animas(loading = True, txt = '%s Выход на поисковую строку' % (self.r_text_back_a))
				i.brower_search()
			else:
				i.animas(txt = '%s Простите но ваш запрос некорректен...' % (self.r_text_back_a))
				i.animas(loading = True, txt = '%s Подождите немного' % (self.r_text_back_a))
				i.brower_output()
	pass
class Command_importing(Error): 
	def log_run(self, com):
		if com == '__text__':
			self.ModeFic_global[3].append(self.txting)
			self.txting, self.txting2 = '', ''
			self.txt = self.mode.read(1)
			if self.developer_mode == True:
				i.mini_function('developer_import_info')
			if self.txt == '{':
				while self.txt != '}':
					self.txt = self.mode.read(1)
					if self.developer_mode == True:
						i.mini_function('developer_import_info')
					if self.txt == '<':
						if self.txting2 == None:
							while self.txt != '>':
								self.txt = self.mode.read(1)
								if self.developer_mode == True:
									i.mini_function('developer_import_info')
								if self.txt != '>':
									self.txting += self.txt
								i.print_importing()
						else:
							for y in range(len(self.ModeFic_global[7])):
								if self.txting2 == self.ModeFic_global[7][y]:
									self.txting2 == self.ModeFic_global[8][y]
									break
							self.txting += self.txting2
							self.txting2 = ''
							self.mode.seek(self.mode.tell() - 1)
					elif self.txt == '}':
						if self.txting2 != None:
							for y in range(len(self.ModeFic_global[7])):
								if self.txting2 == self.ModeFic_global[7][y]:
									self.txting2 = self.ModeFic_global[8][y]
									break
							self.txting += self.txting2
							self.txting2 = ''
							self.mode.seek(self.mode.tell() - 1)
					else:
						if self.txt != '>' and\
						self.txt != '\n' and\
						self.txt != '\t':
							self.txting2 += self.txt
					i.print_importing()
class II(Command_importing, Brower, Console, Error): # Глобальный класс для клиента
	# Начало Start
	def __init__(self): # Постоянно активная функция для переменных
		self.dir_python_file = os.getcwd() # Директория в которой находится исполняемый python фаил
		self.MP3_Hello_file = pygame.mixer.Sound('%s/Mp3_QRTG-effects/client_start.mp3' % (self.dir_python_file)) # Начало работы файла - приветствие
		self.MP3_Bye_file = pygame.mixer.Sound('%s/Mp3_QRTG-effects/Bye_Doun.mp3' % (self.dir_python_file)) # Окончание работы файла - прощание
		self.MP3_Open_account = pygame.mixer.Sound('%s/Mp3_QRTG-effects/Open_account.mp3' % (self.dir_python_file)) # Успешный вход в аккаунт
		self.MP3_Open = pygame.mixer.Sound('%s/Mp3_QRTG-effects/Open.mp3' % (self.dir_python_file)) # Включение
		self.MP3_Off = pygame.mixer.Sound('%s/Mp3_QRTG-effects/Close.mp3' % (self.dir_python_file)) # Выключение
		self.MP3_Denial = pygame.mixer.Sound('%s/Mp3_QRTG-effects/Denial.mp3' % (self.dir_python_file)) # Отрицание
		self.MP3_Complete = pygame.mixer.Sound('%s/Mp3_QRTG-effects/Complete.mp3' % (self.dir_python_file)) # Удачное завершение процесса
		self.MP3_Warning = pygame.mixer.Sound('%s/Mp3_QRTG-effects/Warning.mp3' % (self.dir_python_file)) # Предупреждение
		self.MP3_Crash = pygame.mixer.Sound('%s/Mp3_QRTG-effects/System_crash.mp3' % (self.dir_python_file)) # Краш
		self.MP3_Error = pygame.mixer.Sound('%s/Mp3_QRTG-effects/Error.mp3' % (self.dir_python_file)) # Ошибка
		self.MP3_Client_byebye = pygame.mixer.Sound('%s/Mp3_QRTG-effects/client_bye-bye.mp3' % (self.dir_python_file)) # Завершение работы клиента QRTG
		self.MP3_Test_volume = pygame.mixer.Sound('%s/Mp3_QRTG-effects/Test_volume.mp3' % (self.dir_python_file)) # Проверка громкости QRTG
		self.exit_gl_command = 0 # Выход из глобальных команд (0;1)
		self.ipp_txt = None # Сохраняемый символ под индикатор окончания при чтении фаила
		self.ipp = None # Системный невозврат - индекс
		self.pol_name = '' # Полное имя
		self.gl_time = localtime() # Точное время
		self.version = None # Версия клиента
		self.x = 0 # Индекс для списков в цикле "for"
		self.ip_ass = 0 # Индекс для импортирования (0 - нет импорта ; 1 - идёт импорт ; 'end' - закончен ; 3 - ошибка 0g7508)
		self.indif = '0' # Какой импорт по количеству модов ('all' - все;'Nall' - один)
		self.answer = None # Ответ На строке или вопрос
		self.console_programm = 0 # Является ли команда консольной? (0-False;1-None;2-True)
		self.name = None # Имя аккаунта
		self.txt = 0 # Символ в текстовом документе
		self.txting = '' # Слово или текст для "self.txt"
		self.txting2 = '' # Запасная запись self.txting переменной при чтении фаила
		self.txting3 = '' # Запасная запись self.txting переменной при чтении фаила
		self.txting_check = None # Проверяющее слово или текст для "self.txt"
		self.txting_N = None # Запись какого-нибудь значения при чтении фаила
		self.position = None # Место нахождения
		self.password = None # Пароль от аккаунта
		self.pre_coin_Q = 0 # Прошлая стоимость qC
		self.val = None # Индикатор валюты для банка
		self.pos_txt_coin = 0 # Позиция записи значения в определённую переменную при проверки биржи
		self.number_pos_txt = None # Позиция записи значения в определённую переменную при регистрации
		self.pos_txt_system = 0 # Запись номера отсчёта в системной команде при чтении
		self.console_mode_activate = False # Обновили ли пакет модов (True;False)
		self.number_pos = 0 # Позиция подсчёта команд при чтении
		self.mon = None # Определитель месяца
		self.printing_time = None # Вывод полноценного времени и даты
		self.random_global_number_save = None # Любое сохранённое рандомное число
		self.open_new = None # Какое открытие заголовка новое или нет (1;0)
		self.import_act = None # Какой мод импортируется Последний или нет (True;False)
		self.N = None # Значение формулы "3N+1 and N/2"
		self.att = 0 # Подсчёт повторений для всего
		self.cv_file_full = None # Сколько всего символов из файлов импорта по номеру для чтения
		self.printing_import_text = None # Текст загрузки для импорта
		self.sdi = None # Скорость интернета QRTG (действия в секунду)
		self.stoping = 0 # Торможения интернета QRTG
		self.print_global_text = None # Любой выводимый текст
		self.audio_vol = None # Громкость звуков в клиенте
		self.audio_channel = pygame.mixer.find_channel() # Аудио канал для звуков QRTG
		if os.path.isfile('%s/TF/RebootinformationpanelQRTG.tf' % (self.dir_python_file)) != True:
			self.chill_change = None # Управляющая переменная файлом "Chill_change.py"
		self.chill_change_return = 0 # Включен ли фаил "Chill_change.py" (1;0)
		self.settings_master = 0 # Включён ли режим "master" в настройках QRTG (1;0)
		self.sleep_night = 0 # Запрет активации QRTG ночью (1;0)
		self.clear_console = lambda: os.system('cls') # Очистка консоли
		self.developer_mode = False # Режим разработчика (True;False)
		self.save_data_all = True # Сохраняются ли данные автоматически (True;False)
		self.Magic_loading = [] # Магическая загрузка
		self.Magic_loading2 = [] # Магическая загрузка 2
		self.desktop_log = 0 # Анимация фонового времени (0;3)
		self.all_commands = [] # Все команды записываемые из "0_6.viu"
		self.command_txting = False # Совпадает ли команда из мода с системной (True;False)
		self.activate_magic_loading = False # Включена ли магическая загрузка (True;False)
		self.text_invisible = ' ' # Невидимый текст для паролей
		self.loading_sym = ['/','—','\\','|'] # Символы загрузки
		self.loading_default = [] # Обысчная закрузка (по кадрово)
		self.visual_end_reading_modes = False # Визуальное окончание чтения модов (True;False)
		self.exit_file = False # Выход из файла (True;False)
		self.re_boot = 0 # Произойдёт ли перезагрузка клиента (1;0)
		self.print_text_global = '' # Выводимый текст для приложения
		self.logic_control = ['None'] # Управление логикой и функциями, значения см. в справочник. (*0300)
		self.brower_chrome = None # Браузер для общедоступных данных
		# internet \/ -----------------------------------------------------------------------------------------------------------------------------------------------------------|
		self.internet_text_input = [] # Задаваемый текст для подсимвольного вывода
		self.internet_text_output = None # Подсимвольный вывод текста
		self.internet_text_output_saving = None # Сохранившийся подсимвольный текст
		self.internet_global_activation = None # Работает ли интернет QRTG (True;False)
		self.internet_exit_read_file = 0 # Конец чтения файла .javas
		self.internet_indification = [] # На что распространяется интернет
		self.internet_protocol = None # Протокол на который ссылается в браузере интернет
		self.internet_coding = [] # Какой вид кодировки интернета
		self.internet_start_str = None # Начальная страница в браузере
		self.internet_text = None # Выводимый текст в браузере
		self.internet_searching = None # Недавние поиски от пользователя
		self.internet_searching_list = [] # Список недавних поисков от пользователя
		self.internet_link = None # Ссылка в брвузере
		# internet /\ ----------------------------------------------------------------------------------------------------------------------------------------------------------|
		# save \/ --------------------------------------------------------------------------------------------------------------------------------------------------------------|
		self.Saving_Global_data = [] # Запись определённых сохраняемых переменных и распределение при открытии клиента
		# save /\ --------------------------------------------------------------------------------------------------------------------------------------------------------------|
		# coin \/ --------------------------------------------------------------------------------------------------------------------------------------------------------------|
		self.Q = 0 # Баланс qC
		self.coin_Q = None # Стоимость qC
		self.active_coin_Q = None # Изменяется ли qC (True;False)
		self.ruble = 0 # Баланс ruble
		self.coin_ruble = None # Стоимость ruble
		self.active_coin_ruble = None # Изменяется ли ruble (True;False)
		self.global_t = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]# 0 - qC, 1 - ruble, 2 - rate, 3 - global_com (Время: отсчёта, сравнения, проверки)
		self.coin_ruble_Q_pos = False # Изменилась ли цена валют "ruble" и "Q" (True;False)
		self.ans_value = None # Название валюты для проверки
		self.cheque = None # Чек
		self.rate_name = [] # Ники пользователей, названия ставок
		self.rate_price = [] # Цена ставок
		self.rate_price_coin = [] # Валюта для цены ставок
		self.rate_profit = [] # Прибыль ставок
		self.rate_profit_coin = [] # Валюта для прибыли ставок
		self.rate_random_number = None # Случайное число для ставок
		self.rate_change = True # Изменяются ли ставки "ruble" и "Q" (True;False)
		self.rate_random_name = [] # Случайное имя для продавца
		self.rate_equally_name = False # Совпадают ли имена в rate_name и rate_random_name (True;False)
		self.rate_len = 0 # Последний элемент для списка
		self.rate_ipp = None # Строка логического "Если" при проверки (число от нуля)
		self.rate_update = 0 # Надо ли обновлять ставки повторно (1;0)
		self.if_for_global = None # Проверка False или True в "for"
		# coin /\ --------------------------------------------------------------------------------------------------------------------------------------------------------------|
		# Modes \/ -------------------------------------------------------------------------------------------------------------------------------------------------------------|
		#\/
		self.global_command_number_system = -1 # номер системной команды ровно по списку при чтении
		self.mode = None # Импортированный мод
		self.read_mode_import = None # Импортируемый мод
		self.len_ModeFic_expl = 0 # Была ли произведена запись в expl (1;0)
		self.expl_indification = None # В какую позицию списка записано пояснение команды
		self.import_command = None # Какая команда импортируется
		self.ModeFic_global = [] # Modefic список всех видов, см в справочник
		# Modes /\ -------------------------------------------------------------------------------------------------------------------------------------------------------------|
		# Change \/ ------------------------------------------------------------------------------------------------------------------------------------------------------------|
		self.r_text_name_global_var = ['self.r_text_back_a', 'self.r_text_back_b', 'self.r_text_back_c', 'self._r_text_a','self.r_text_back_transition'] # Названия текстовых переменных
		self.r_text_id_global_var = ['AA00001','AA00002','AA00003','AA00004','AA00005'] # Коды для распознания переменной
		self.r_text_QRTG = ['>>>', 'QRTG-Client', '...', '->'] # Настройки текста по умолчанию
		self.r_text_back_a = '>>>' # Начало всего системного текста в QRTG-Clien
		self.r_text_back_b = 'QRTG-Client' # Имя файла как имени обращения
		self.r_text_back_c = '...' # Окончание сообщения как с молчанием
		self.r_text_back_transition = '->' # Переход текста
		self.tf_information = None # Временные значения, кеш-память
		# Change /\ ------------------------------------------------------------------------------------------------------------------------------------------------------------|
	def ModeFic_clear(self, set_ipp = None):
		if set_ipp == 9:
			self.ModeFic_global[1] = []
			self.ModeFic_global[2] = []
			self.ModeFic_global[3] = []
			self.ModeFic_global[4] = []
			self.ModeFic_global[5] = []
			self.ModeFic_global[6] = []
			self.ModeFic_global[7] = []
			self.ModeFic_global[8] = []
			self.ModeFic_global[9] = []
			self.ModeFic_global[11] = []
			self.ModeFic_global[12] = []
		elif set_ipp == 13:
			self.ModeFic_global[0] = []
			self.number_pos = 0
			self.global_command_number_system = -1
			self.console_mode_activate = False
		else:
			i.error('0g7503')
		if self.save_data_all == True:
			i.saving_data('Data_mode')
	def mode_command_check(self):
		activate = None
		if len(self.ModeFic_global[1]) > 0:
			for self.x in range(len(self.ModeFic_global[1])):
				if self.x < len(self.ModeFic_global[1]):
					if self.answer == self.ModeFic_global[1][self.x]:
						activate = True
						break
		if activate == True:
			if self.console_programm != 4:
				i.mode_activate()
			else:
				if len(self.ModeFic_global[12]) > 0:
					if self.ModeFic_global[12][int(self.ModeFic_global[5][self.x])] == '0':
						print('%s Мод-команда "%s" является для %s из мода неизвестной' % (self.r_text_back_a, self.answer, self.r_text_back_b))
					else:
						print('%s Мод-команда "%s" отвечает за "%s"' % (
						self.r_text_back_a, self.answer, self.ModeFic_global[12][int(self.ModeFic_global[5][self.x])]
						))
					return True
		else:
			if self.console_programm != 4:
				i.error('0g7502')
	def start_job(self): # Начало работы или старт клиента
		self.audio_channel.play(self.MP3_Hello_file)
		self.file = open('%s/Saven.dll' % (self.dir_python_file))
		while self.txt != '.':
			self.txt = self.file.read(1)
			if self.developer_mode == True:
				print('self.txt: <%s>' % (self.txt))
				print('self.txting: <%s>\n' % (self.txting))
			elif self.txt == ';' or self.txt == '.':
				self.Saving_Global_data.append(self.txting)
				self.txting = ''
			else: self.txting += self.txt
		self.file.close()
		for y in range(len(self.Saving_Global_data)):
			if y == 0: self.pos_txt_system = int(self.Saving_Global_data[y])
			elif y == 1: self.number_pos = int(self.Saving_Global_data[y])
			elif y == 2: self.global_command_number_system = int(self.Saving_Global_data[y])
			elif y == 3: self.chill_change_return = int(self.Saving_Global_data[y])
			elif y == 4: self.sleep_night = int(self.Saving_Global_data[y])
			elif y == 5:
				if self.Saving_Global_data[y] == 'True': self.developer_mode = True
				else: self.developer_mode = False
			elif y == 6:
				if self.Saving_Global_data[y] == 'True': self.save_data_all = True
				else: self.save_data_all = False
			elif y == 7:
				if self.Saving_Global_data[y] == 'True': self.activate_magic_loading = True
				else: self.activate_magic_loading = False
			elif y == 8: self.desktop_log = int(self.Saving_Global_data[y])
		if os.path.isfile('%s/TF/RebootinformationpanelQRTG.tf' % (self.dir_python_file)) == True:
			self.file = open('%s/TF/RebootinformationpanelQRTG.tf' % (self.dir_python_file))
			self.tf_information = self.file.read()
			self.file.close()
			os.remove('%s/TF/RebootinformationpanelQRTG.tf' % (self.dir_python_file))
		if self.tf_information != 'REBOOT':
			if self.chill_change_return == 1:
				self.chill_change = subprocess.Popen([sys.executable, 'Chill_change.py'])
		else:
			self.tf_information = None
		self.file.close()
		i.animas(loading = True, txt = '%s Подготовка к работе %s' % (self.r_text_back_a, self.r_text_back_b))
		coin = open('%s/Coin.txt' % (self.dir_python_file))
		while self.txt != '{':
			self.txt = coin.read(1)
			if self.txt == ';' or self.txt == '{':
				if self.pos_txt_coin == 0:
					self.coin_Q = int(self.txting)
				elif self.pos_txt_coin == 1:
					if self.txting == 'True': self.active_coin_Q = True
					elif self.txting == 'False': self.active_coin_Q = False
				elif self.pos_txt_coin == 2:
					self.coin_ruble = int(self.txting)
				elif self.pos_txt_coin == 3:
					if self.txting == 'True': self.active_coin_ruble = True
					elif self.txting == 'False': self.active_coin_ruble = False
				self.txting = ''
			else:
				self.pos_txt_coin += 1
				self.txting += self.txt
		while self.txt != '}':
			if self.txt == '{':
				while self.txt != ':':
					self.txt = coin.read(1)
					if self.txt == ':':
						self.Q = self.txting
					else:
						self.txting += self.txt
				while self.txt != '}':
					self.txt = coin.read(1)
					if self.txt == '}':
						self.ruble = self.txting
					else:
						self.txting += self.txt
		self.pos_txt_coin, self.txting = 0, ''
		coin.close()
		i.animas(txt = '%s Чтение вашего паспорта %s...' % (self.r_text_back_a, self.r_text_back_b))
		system = open('%s/SYSTEM.txt' % (self.dir_python_file))
		self.txt = system.read(1)
		if self.txt == '#':
			while self.txt != '.':
				self.txt = system.read(1)
				if self.txt == '{':
					self.name = self.txting
					self.txt, self.txting = None, ''
				elif self.txt == '}':
					self.password = self.txting
				elif self.txt == '~':
					self.txt = None
					while self.txt != '~':
						self.txt = system.read(1)
						if self.txt != '~':
							self.pol_name += self.txt
				else:
					self.txting += self.txt
		system.close()
		self.txt, self.txting = None, ''
		i.animas(txt = '%s Чтение .viu файлов...' % (self.r_text_back_a))
		list_info = ['0_1.viu','0_6.viu','0_7.viu']
		for self.x in list_info:
			i.jik_read(self.x, open('%s/Viu/%s' % (self.dir_python_file, self.x)))
		i.animas(txt = '%s Чтение модов...' % (self.r_text_back_a))
		if self.position != 'ERROR':
			self.txt, self.txting, new_command_list = None, '', True
			num_list = 0
			self.file = open('%s/Saven_Mods.dll' % (self.dir_python_file))
			while self.txt != '!':
				self.txt = self.file.read(1)
				if self.txt == '[':
					while self.txt != ']':
						self.txt = self.file.read(1)
						if self.txt == '[':
							while self.txt != ']':
								self.txt = self.file.read(1)
								if self.developer_mode == True:
									print('txt = <%s>' % (self.txt))
									print('txting = <%s>' % (self.txting))
								if self.txt == ',' or self.txt == ']':
									if self.txting != '':
										if new_command_list == True:
											self.ModeFic_global.append([self.txting])
										else:
											self.ModeFic_global[num_list].append(self.txting)
										if self.developer_mode == True:
											print('list! [%s] (%s)' % (num_list, self.txting))
											sleep(0.8)
									else:
										if self.txt == ']' and self.txting == '':
											self.ModeFic_global.append([])
									if self.txt == ',':
										self.file.read(1)
									new_command_list, self.txting = False, ''
								else:
									if self.txt != "'" and\
									self.txt != '[':
										self.txting += self.txt
							self.txt = None
						elif self.txt == ',':
							num_list += 1
							new_command_list = True
			if self.file.tell() == 1 and self.txt == '!':
				self.console_mode_activate = False
				self.ModeFic_global = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
				self.pos_txt_system = 0
			self.file.close()
			if self.developer_mode == True:
				print('\n%s' % (self.ModeFic_global))
			i.animas(txt = '%s Создание анимаций...' % (self.r_text_back_a))
			self.txt, self.txting, self.file = None, '', open('%s/Loading.txt' % (self.dir_python_file))
			while True:
				self.txt = self.file.read(1)
				if self.developer_mode == True:
					print('-----')
					print('True')
					print('self.file = Loading.txt')
					print('self.txt = %s' % (self.txt))
					print('self.txting = %s\n' % (self.txting))
				if self.txt == '%':
					index_loading = self.txting
					self.txt, self.txting = None, ''
					while self.txt != ']':
						self.txt = self.file.read(1)
						if self.developer_mode == True:
							print('default')
							print(']')
							print('self.file = Loading.txt')
							print('self.txt = %s' % (self.txt))
							print('self.txting = %s\n' % (self.txting))
						if self.txt == ',' or self.txt == ']':
							if self.developer_mode == True:
								print('Append = "%s"\n' % (self.txting))
							if index_loading == 'default':
								self.loading_default.append(self.txting)
							elif index_loading == '1':
								self.Magic_loading.append(self.txting)
							elif index_loading == '2':
								self.Magic_loading2.append(self.txting)
							self.txting = ''
						else:
							if self.txt != '[' and\
							self.txt != "'" and\
							self.txt != ',' and\
							self.txt != '\t' and\
							self.txt != '\n':
								self.txting += self.txt
					if self.developer_mode == True:
						print(self.txting == 'default')
						print(self.txting == '1')
						print(self.txting == '2',end='\n\n')
				elif self.txt == '!':
					break
				else:
					if self.txt != '\t' and\
					self.txt != '\n':
						self.txting += self.txt
			self.file.close()
			i.animas(txt = '%s Подключение %s интернета...' % (self.r_text_back_a, self.r_text_back_b))
			self.txt, self.txting = None, ''
			self.file = open('%s/Internet QRTG/Pall.javas' % (self.dir_python_file))
			while True:
				if self.developer_mode == True:
					print('-----')
					print('self.txt = %s' % (self.txt))
					print('self.txting = %s\n' % (self.txting))
				self.txt = self.file.read(1)
				if self.txt == '.':
					if self.txting == 'internet':
						self.txt, self.txting = None, ''
						while self.txt != ')':
							if self.developer_mode == True:
								print('internet')
								print('self.txt = %s' % (self.txt))
								print('self.txting = %s\n' % (self.txting))
							self.txt = self.file.read(1)
							if self.txt == '(' or self.txt == '.':
								if self.txting == 'global':
									self.txt, self.txting = None, ''
									while self.txt != ')':
										if self.developer_mode == True:
											print('internet.global')
											print('self.txt = %s' % (self.txt))
											print('self.txting = %s\n' % (self.txting))
										self.txt = self.file.read(1)
										if self.txt == ')':
											if self.txting.isnumeric() == True:
												if int(self.txting) <= 0:
													self.internet_global_activation = False
												else:
													self.internet_global_activation = True
											else:
												if self.txting == 'F':
													self.internet_global_activation = False
												elif self.txting == 'T':
													self.internet_global_activation = True
											self.txting = ''
										else:
											if self.txt != ' ' and\
											self.txt != '\n' and\
											self.txt != '\t':
												self.txting += self.txt
								elif self.txting == 'portal':
									self.txt, self.txting = None, ''
									while self.txt != ')':
										if self.developer_mode == True:
											print('internet.portal')
											print('self.txt = %s' % (self.txt))
											print('self.txting = %s\n' % (self.txting))
										self.txt = self.file.read(1)
										if self.txt == ')':
											self.internet_protocol = self.txting
											self.txting = ''
										else:
											if self.txt != ' ' and\
											self.txt != '\n' and\
											self.txt != '\t':
												self.txting += self.txt
								elif self.txting == 'system':
									if self.txt == '.':
										self.txting = ''
										self.txt = self.file.read(1)
										if self.developer_mode == True:
											print('System -> %s <- %s' % (self.txt, self.internet_global_activation))
										if self.txt == '0' or self.txt == 'F':
											if self.internet_global_activation == False:
												self.txt = self.file.read(1)
												if self.txt == '(':
													while self.txt != ')':
														if self.developer_mode == True:
															print('internet.system F')
															print('self.txt = %s' % (self.txt))
															print('self.txting = %s\n' % (self.txting))
														self.txt = self.file.read(1)
														if self.txt == ')':
															if self.txting == 'close':
																self.internet_exit_read_file = 1
																self.txting = ''
														else:
															if self.txt != ' ' and\
															self.txt != '\n' and\
															self.txt != '\t':
																self.txting += self.txt
											else:
												self.txt, self.txting = None, ''
												if self.developer_mode == True:
													print('System !-> F')
												while self.txt != ')':
													self.txt = self.file.read(1)
										elif self.txt == '1' or self.txt == 'T':
											if self.internet_global_activation == True:
												self.txt = self.file.read(1)
												if self.txt == '(':
													while self.txt != ')':
														if self.developer_mode == True:
															print('internet.system T')
															print('self.txt = %s' % (self.txt))
															print('self.txting = %s\n' % (self.txting))
														self.txt = self.file.read(1)
														if self.txt == ')':
															if self.txting == 'close':
																self.internet_exit_read_file = 1
														else:
															if self.txt != ' ' and\
															self.txt != '\n' and\
															self.txt != '\t':
																self.txting += self.txt
											else:
												self.txt, self.txting = None, ''
												if self.developer_mode == True:
													print('System !-> F')
												while self.txt != ')':
													self.txt = self.file.read(1)
							else:
								if self.txt != ' ' and\
								self.txt != '\n' and\
								self.txt != '\t':
									self.txting += self.txt
					elif self.txting == 'un':
						self.txting = ''
						while self.txt != ')':
							if self.developer_mode == True:
								print('un')
								print('self.txt = %s' % (self.txt))
								print('self.txting = %s\n' % (self.txting))
							self.txt = self.file.read(1)
							if self.txt == '(':
								if self.txting == 'system':
									self.txting = ''
									while self.txt != ')':
										if self.developer_mode == True:
											print('un.system')
											print('self.txt = %s' % (self.txt))
											print('self.txting = %s\n' % (self.txting))
										self.txt = self.file.read(1)
										if self.txt == ')':
											if self.txting == 'file' or self.txting == 'brower':
												self.internet_indification.append(self.txting)
												self.txting = ''
										else:
											if self.txt != ' ' and\
											self.txt != '\n' and\
											self.txt != '\t':
												self.txting += self.txt
								elif self.txting == 'coding':
									self.txting = ''
									while self.txt != ')':
										if self.developer_mode == True:
											print('un.coding')
											print('self.txt = %s' % (self.txt))
											print('self.txting = %s\n' % (self.txting))
										self.txt = self.file.read(1)
										if self.txt == ')':
											if self.txting == 'QRTG' or self.txting == 'LR-global':
												if self.developer_mode == True:
													print('un.coding')
													print('code_language - system')
													print('Append - True\n')
												self.internet_coding.append(self.txting)
											else:
												if self.developer_mode == True:
													print('un.coding')
													print('code_language - Unknown')
													print('Append - False\n')
											self.txting = ''
										else:
											if self.txt != ' ' and\
											self.txt != '\n' and\
											self.txt != '\t':
												self.txting += self.txt
								elif self.txting == 'start':
									self.txting = ''
									while self.txt != ')':
										if self.developer_mode == True:
											print('un.start')
											print('self.txt = %s' % (self.txt))
											print('self.txting = %s\n' % (self.txting))
										self.txt = self.file.read(1)
										if self.txt == ')':
											self.internet_start_str = self.txting
											self.txting = ''
										else:
											if self.txt != ' ' and\
											self.txt != '\n' and\
											self.txt != '\t':
												self.txting += self.txt
							else:
								if self.txt != ' ' and\
								self.txt != '\n' and\
								self.txt != '\t':
									self.txting += self.txt
				elif self.txt == '#':
					self.txt, self.txting = None, ''
					while self.txt != '#':
						self.txt = self.file.read(1)
				else:
					if self.txt != ' ' and\
					self.txt != '\n' and\
					self.txt != '\t':
						self.txting += self.txt
				if self.internet_exit_read_file == 1:
					self.internet_exit_read_file = 0
					break
			self.file.close()
			if self.developer_mode == True:
				print(self.internet_protocol)
				print(self.internet_indification)
				print(self.internet_global_activation)
				print(self.internet_exit_read_file)
		else:
			i.animas(txt = '%s Сохранённые данные модов неправильно записаны...' % (self.r_text_back_a))
			sleep(0.5)
			i.exit_poduct()
		if self.exit_file != True:
			if len(self.ModeFic_global) != 0:
				if len(self.ModeFic_global[11]) == len(self.ModeFic_global[0]):
					if len(self.ModeFic_global[11]) != 0 and len(self.ModeFic_global[0]) != 0:
						self.console_mode_activate = True
			else:
				self.console_mode_activate = False
			if self.name == 0 or self.name == None or self.name == 'None':
				list_info = ['ое утро','ый день','ый вечер','ой ночи']
				if self.gl_time[3] >= 6 and self.gl_time[3] <= 12:
					i.animas(txt = '%s Добр%s пользователь!' % (self.r_text_back_a, list_info[0]))
				elif self.gl_time[3] >= 13 and self.gl_time[3] <= 18:
					i.animas(txt = '%s Добр%s пользователь!' % (self.r_text_back_a, list_info[1]))
				elif self.gl_time[3] >= 19 and self.gl_time[3] <= 23:
					i.animas(txt = '%s Добр%s пользователь!' % (self.r_text_back_a, list_info[2]))
				elif self.gl_time[3] >= 0 and self.gl_time[3] <= 5:
					i.animas(txt = '%s Добр%s пользователь!' % (self.r_text_back_a, list_info[3]))
				if self.sleep_night == 1 and self.gl_time[3] >= 0 and self.gl_time[3] <= 5:
					i.mini_function('sleep')
				else:
					i.animas(txt = '%s Вы не зарегестрированы на %s, пожалуйста зарегестрируйтесь' % (self.r_text_back_a, self.r_text_back_b))
					self.position, self.number_pos_txt = 'Register', '1'
					i.register()
			else:
				list_info = ['ое утро','ый день','ый вечер','ой ночи']
				if self.gl_time[3] >= 6 and self.gl_time[3] <= 12:
					i.animas(txt = '%s Добр%s %s!' % (self.r_text_back_a, list_info[0], self.pol_name))
				elif self.gl_time[3] >= 13 and self.gl_time[3] <= 18:
					i.animas(txt = '%s Добр%s %s!' % (self.r_text_back_a, list_info[1], self.pol_name))
				elif self.gl_time[3] >= 19 and self.gl_time[3] <= 23:
					i.animas(txt = '%s Добр%s %s!' % (self.r_text_back_a, list_info[2], self.pol_name))
				elif self.gl_time[3] >= 0 and self.gl_time[3] <= 5 and self.sleep_night == 0:
					i.animas(txt = '%s Добр%s %s!' % (self.r_text_back_a, list_info[3], self.pol_name))
				i.password_account(True)
	def jik_read(self, file, system_info): # Чтение системных индекаторов-файлов .viu
		self.answer = file
		if file == '0_1.viu':
			while self.txt != '!':
				self.txt = system_info.read(1)
				if self.txt == '{':
					if self.txting == 't':
						self.txting = ''
						while self.txt != '}':
							self.txt = system_info.read(1)
							if self.txt == '-':
								if self.txting == 'ver':
									self.txting = ''
									while self.txt != ';':
										self.txt = system_info.read(1)
										if self.txt == ';':
											self.version = self.txting
											self.txting = ''
										else:
											self.txting += self.txt
								else:
									i.error('0g7509')
									sleep(0.2)
									if self.txting.find('ver') != -1:
										i.animas(txt = '%s Текст похож на ключевое слово (ver) исправте ошибку' % (self.r_text_back_a))
									else:
										i.animas(txt = '%s Не удалось выявить похожие ключевые слова для ошибочного текста' % (self.r_text_back_a))
									sleep(1)
									i.exit_poduct()
							else:
								self.txting += self.txt
					else:
						i.error('0g7509')
						sleep(0.2)
						if self.txting.find('t') != -1:
							i.animas(txt = '%s Текст похож на ключевое слово (t) исправте ошибку' % (self.r_text_back_a))
						else:
							i.animas(txt = '%s Не удалось выявить похожие ключевые слова для ошибочного текста' % (self.r_text_back_a))
						sleep(2)
						i.exit_poduct()
				else:
					self.txting += self.txt
		elif file == '0_4.viu':
			while self.txt != ';':
				self.txt = system_info.read(1)
				if self.txt == ';':
					self.audio_vol, self.txting = float(self.txting), ''
				else:
					if self.txt != '{':
						self.txting += self.txt
		elif file == '0_6.viu':
			new_command_list = True
			while self.txt != '.':
				self.txt = system_info.read(1)
				if self.txt == '\n' or self.txt == '.' or self.txt == ',':
					if self.txting != '':
						if new_command_list == True:
							self.all_commands.append([self.txting])
							new_command_list = False
						else:
							if self.txt == '\n':
								new_command_list = True
							self.all_commands[len(self.all_commands) - 1].append(self.txting)
					self.txting = ''
				else:
					if self.txt != '\n' and\
					self.txt != '\t' and\
					self.txt != '.' and\
					self.txt != ' ':
						self.txting += self.txt
			if self.developer_mode == True:
				print(self.all_commands)
		elif file == '0_7.viu':
			while self.txt != '.':
				self.txt = system_info.read(1)
				if self.txt == ',' or self.txt == '.':
					if self.txting != '':
						self.rate_random_name.append(self.txting)
					self.txting = ''
				else:
					if self.txt != '\n' and\
					self.txt != '\t' and\
					self.txt != '.' and\
					self.txt != ' ':
						self.txting += self.txt
			if self.developer_mode == True:
				print(self.all_commands)
				print(self.rate_random_name)
		system_info.close()
		self.txt, self.txting = None, ''
	def password_account(self, start_fun = False): # Ввод пароля пользователя
		if start_fun == True:
			att_account = 0
			if randint(0, 1) == 1:
				if self.gl_time[3] >= 6 and self.gl_time[3] <= 12:
					self.internet_text_input = '%s Наверно вы выспались %s' % (self.r_text_back_a, self.pol_name)
				elif self.gl_time[3] >= 13 and self.gl_time[3] <= 18:
					self.internet_text_input = '%s Эх %s, работа-работа...' % (self.r_text_back_a, self.pol_name)
				elif self.gl_time[3] >= 19 and self.gl_time[3] <= 23:
					self.internet_text_input = '%s Именно %s, добрейший вечерочек)' % (self.r_text_back_a, self.pol_name)
				elif self.gl_time[3] >= 0 and self.gl_time[3] <= 5:
					self.internet_text_input = '%s %s наверно вы устали...' % (self.r_text_back_a, self.pol_name)
				i.animas(txt = self.internet_text_input)
		if self.sleep_night == 1 and self.gl_time[3] >= 0 and self.gl_time[3] <= 5:
			i.mini_function('sleep')
		else:
			if self.developer_mode == True:
				print(self.ModeFic_global[0], 'Имя загруженных модов')
				print(self.ModeFic_global[1], 'Имя команд')
				print(self.ModeFic_global[2], 'Название действий в команде')
				print(self.ModeFic_global[3], 'Итог действий в команде')
				print(self.ModeFic_global[4], 'Кол-во действий в команде')
				print(self.ModeFic_global[5], 'Начало отсчёта действий в команде')
				print(self.ModeFic_global[6], 'Место выполнения команды')
				print(self.ModeFic_global[7], 'Имя переменных')
				print(self.ModeFic_global[8], 'Значения переменных')
				print(self.ModeFic_global[9], 'Итог вывода сообщения о спящем режиме')
				print(self.ModeFic_global[10], 'Записываемый текст в log.log')
				print(self.ModeFic_global[11], 'Имя импортированных модов')
				print(self.ModeFic_global[12], 'Поянение команд из модов')
			i.animas(n = 1, txt = 'Введите пароль от аккаунта %s:' % (self.name))
			self.answer = input('Введите пароль от аккаунта %s: ' % (self.name))
			if self.answer == self.password:
				if self.active_coin_Q == True:
					self.global_t[0][0] = time()
				if self.active_coin_ruble == True:
					self.global_t[1][0] = time()
				self.global_t[2][0] = time()
				self.audio_channel.play(self.MP3_Open_account)
				i.animas(txt = '%s Добро пожаловать %s' % (self.r_text_back_a, self.name))
				i.animas(txt = '%s Версия %s "%s"' % (self.r_text_back_a, self.r_text_back_b, self.version))
				if att_account >= 4:
					print('%s %s, пожалуйста запомните свой пароль от аккаунта... Это важно' % (self.r_text_back_a, self.pol_name))
				self.ipp = None
				i.main_menu()
			elif len(self.answer) == 0:
				self.audio_channel.play(self.MP3_Bye_file)
				if self.chill_change_return == 1:
					self.chill_change.kill()
					self.chill_change_return = 0
				i.exit_poduct()
			else:
				print('%s Ваш пароль не совпадает с набраным - повторите попытку' % (self.r_text_back_a))
				self.audio_channel.play(self.MP3_Denial)
				att_account += 1
				if att_account == 6:
					log_txt = i.mini_function('log')
					log = open('%s/log.log' % (self.dir_python_file), 'w')
					log.write('%s\n%s [%s] Была произведена попытка возможного взлома аккаунта!!!' % (log_txt, self.r_text_back_a, asctime()))
					log.close()
					print('%s Вы произвели 6 попыток ввода пароля, вы возможно мошенник!\n%s Аккаунт заблокирован' % (self.r_text_back_a, self.r_text_back_a))
					sleep(1)
					i.exit_poduct()
				else:
					i.password_account()
	def register(self): #  Регистрация для клиента
		if self.number_pos_txt == '1':
			self.answer = input('Никнейм: ')
			self.name = self.answer
			print('%s Подождите, идёт проверка никнейма...' % (self.r_text_back_a))
			sleep(1)
			if self.name.find('&') != -1: i.error('0g7500', '&')
			elif self.name.find('/') != -1: i.error('0g7500', '/')
			elif len(self.answer) == 0:
				print('%s Никнейм не может быть пустым' % (self.r_text_back_a))
				i.error('0g7500', 0)
				self.audio_channel.play(self.MP3_Denial)
				i.register()
			else:
				self.number_pos_txt = '2'
				print('%s Придумайте пароль для аккаунта' % (self.r_text_back_a))
				self.audio_channel.play(self.MP3_Complete)
				i.register()
		elif self.number_pos_txt == '2':
			self.answer = input('Пароль: ')
			self.password = self.answer
			print('%s Подождите, идёт проверка пароля...' % (self.r_text_back_a))
			sleep(1)
			if self.password.find('&') != -1: i.error('0g7501', '&')
			elif self.password.find('/') != -1: i.error('0g7501', '/')
			elif len(self.answer) == 0:
				print('%s Пароль не может быть пустым' % (self.r_text_back_a))
				i.error('0g7501', 0)
				self.audio_channel.play(self.MP3_Denial)
				i.register()
			else:
				self.number_pos_txt = '3'
				i.register()
		elif self.number_pos_txt == '3':
			self.audio_channel.play(self.MP3_Complete)
			self.answer = input('Введите ваше настоящее имя на Англ.языке (для отказа ничего не пишите): ')
			print('%s Подождите, идёт проверка пользовательского имени...' % (self.r_text_back_a))
			if len(self.answer) == 0:
				print('%s В качестве пользовательского имени будет использовано имя аккаунта' % (self.r_text_back_a))
				self.pol_name = self.name
				i.register()
			else:
				self.pol_name = self.answer
				system = open('%s/SYSTEM.txt' % (self.dir_python_file), 'w')
				system.write('#%s{%s}~%s~.&' % (self.name, self.password, self.pol_name))
				self.audio_channel.play(self.MP3_Open_account)
				print('%s Добро пожаловать %s' % (self.r_text_back_a, self.pol_name))
				system.close()
				if self.active_coin_Q == True:
					self.global_t[0][0] = time()
				if self.active_coin_ruble == True:
					self.global_t[1][0] = time()
				i.main_menu()
	def time_mon(self, mec, day, hour, min, sec): # Создание даты и времени для вывода
		self.gl_time = localtime()
		self.printing_time = '%s Дата:' % (self.r_text_back_a)
		if day < 10:
			self.printing_time += ' 0%s.' % (self.gl_time[2])
		else:
			self.printing_time += ' %s.' % (self.gl_time[2])
		list_info = ['0','Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
		self.mon = list_info[mec]
		if mec < 10:
			self.printing_time += '0%s.' % (self.gl_time[1])
		else:
			self.printing_time += '%s.' % (self.gl_time[1])
		if self.time_week_day.find('Mon') != -1: self.time_week_day = 'Понедельник'
		elif self.time_week_day.find('Tue') != -1: self.time_week_day = 'Вторник'
		elif self.time_week_day.find('Wed') != -1: self.time_week_day = 'Среда'
		elif self.time_week_day.find('Thu') != -1: self.time_week_day = 'Четверг'
		elif self.time_week_day.find('Fri') != -1: self.time_week_day = 'Пятница'
		elif self.time_week_day.find('Sat') != -1: self.time_week_day = 'Суббота'
		elif self.time_week_day.find('Sun') != -1: self.time_week_day = 'Воскресенье'
		self.printing_time += '%sг.\n%s %s/%s\n%s Время:' % (self.gl_time[0], self.r_text_back_a, self.mon, self.time_week_day, self.r_text_back_a)
		self.printing_time += ' %s' % (self.gl_time[3])
		if min < 10:
			self.printing_time += ':0%s' % (self.gl_time[4])
		else:
			self.printing_time += ':%s' % (self.gl_time[4])
		if sec < 10:
			self.printing_time += ':0%sс.' % (self.gl_time[5])
		else:
			self.printing_time += ':%sс.' % (self.gl_time[5])
	def mini_function(self, fun = None):
		if fun == None:
			return 'mini_function end.'
		elif fun == 'menu_console':
			print('%s Такая программа есть в консоли\n%s Выполняем...' % (self.r_text_back_a, self.r_text_back_a))
			sleep(0.6)
		elif fun == 'log':
			log = open('%s/log.log' % (self.dir_python_file))
			log_txt = log.read()
			log.close()
			return log_txt
		elif fun == 'note':
			note = open('%s/note.txt' % (self.dir_python_file))
			note_txt = note.read()
			note.close()
			return note_txt
		elif fun == 'console_end_command':
			if self.console_programm == 0: i.console_start()
			elif self.console_programm == 2: i.main_menu()
		elif fun == 'sleep':
			list_info = ['%s Вам пора спать, утром продолжите работу...' % (self.r_text_back_a),\
			'%s отдыхайте' % (self.r_text_back_a),'%s QRTG заботится о тебе!' % (self.r_text_back_a),\
			'%s Утром ещё встретимся' % (self.r_text_back_a)]
			for self.x in list_info:
				self.internet_text_input = self.x
				i.animas()
			sleep(2)
			i.exit_poduct()
		elif fun == 'developer_import_info':
			print('Position: <%s>' % (self.mode.tell()))
			print('command: <%s>' % (self.import_command))
			print('txt: <%s>' % (self.txt))
			print('txting: <%s>' % (self.txting))
			print('txting2: <%s>' % (self.txting2))
			print('txting3: <%s>' % (self.txting3))
			print('txting_N: <%s>' % (self.txting_N))
			print('txting_check: <%s>' % (self.txting_check))
			print('ipp_txt: <%s>\n' % (self.ipp_txt))
			while keyboard.is_pressed('Alt') != True: pass
			while keyboard.is_pressed('Alt') != False: pass
	def main_menu(self): # Главное меню для клиента
		self.position = 'main_menu'
		self.number_pos_txt = '0'
		self.ipp = None
		i.animas(n = 1, txt = 'Командная строка:')
		self.answer = input('Командная строка: ')
		i.iF_main_menu()
	def iF_main_menu(self): # Проверка команды в главном меню клиента (*0302)
		self.x = 0
		if self.console_programm == 4 and self.developer_mode == True:
			print('+')
		if len(self.answer) == 0 and self.console_programm != 4: i.main_menu()
		elif self.answer == '/' or self.answer == 'console':
			if self.console_programm != 4:
				self.console_programm = 0
				i.console_start()
			else:
				print('%s Команда "%s" отвечает за открытие Консольной строки' % (self.r_text_back_a, self.answer))
				return True
		elif self.answer.find('/') != -1 and self.answer != '/' and self.answer.find('//') == -1:
			if self.console_programm != 4:
				if self.position == 'main_menu':
					print('%s Команда похожа на консольную, проверка в консоли...' % (self.r_text_back_a))
					self.audio_channel.play(self.MP3_Warning)
					sleep(1.2)
					self.console_programm = 2
					i.iF_console()
				else: i.error('0g7502')
			else:
				if i.iF_console() == True: return True
		elif self.answer == 'coin' or self.answer == 'stock market' or self.answer == 'stock' or self.answer == 'market':
			if self.console_programm != 4: i.coin_pr(True)
			else:
				print('%s Команда "%s" отвечает за открытие биржи с прямым каналом' % (self.r_text_back_a, self.answer))
				return True
		elif self.answer == 'bring_out':
			if self.console_programm != 4:
				self.att = 0
				i.Balanse_out_account()
			else:
				print('%s Команда "%s" отвечает за вывод заработанных рублей через чек' % (self.r_text_back_a, self.answer))
				return True
		elif self.answer == 'reboot':
			if self.console_programm != 4:
				if self.save_data_all == True: i.saving_data('ALL')
				i.clear_console()
				i.animas(loading = True, txt = '%s Перезагрузка %s' % (self.r_text_back_a, self.r_text_back_b))
				sleep(1)
				self.re_boot = 1
			else:
				print('%s Команда "%s" отвечает за глобальную перезагрузку системы %s' % (self.r_text_back_a, self.answer, self.r_text_back_b))
				return True
		elif self.answer == 'quit_':
			if self.console_programm != 4: i.exit_file_client()
			else:
				print('%s Команда "%s" отвечает за выход из приложения %s' % (self.r_text_back_a, self.answer, self.r_text_back_b))
				return True
		elif self.answer == 'gl_command' or self.answer == 'glcom' or self.answer == 'gl_com' or self.answer == 'global_com' or self.answer == 'global_command' or self.answer == 'global command' or self.answer == 'help' or self.answer == 'Help' or self.answer == '?':
			if self.console_programm != 4:
				if self.global_t[3][0] != 0:
					self.global_t[3][1] = time()
					self.global_t[3][2] = (self.global_t[3][1]-self.global_t[3][0]) // 120
				if self.global_t[3][0] == 0 or self.global_t[3][2] >= 1:
					self.global_t[3][0] = time()
					print('\n%s Список всех комманд:' % (self.r_text_back_a))
					sleep(0.4)
					for y in self.all_commands:
						self.x = self.all_commands.index(y) + 1
						for y1 in y:
							if y.index(y1) == 0:
								print('%s. "%s,' % (self.x, y1), end = ' ')
							elif y.index(y1) < len(y) - 1:
								print('%s,' % (y1), end = ' ')
							elif y.index(y1) == len(y) - 1:
								if len(y) == 1:
									print('%s. "%s"' % (self.x, y1))
								else:
									print('%s"' % (y1))
						sleep(0.04)
					if len(self.ModeFic_global) > 0:
						if len(self.ModeFic_global[1]) > 0:
							for y in range(0, len(self.ModeFic_global[1])):
								self.x += 1
								print('%s. "%s"' % (self.x, self.ModeFic_global[1][y]))
								sleep(0.04)
				print('\n%s Чтобы выйти отправьте пустое сообщение' % (self.r_text_back_a))
				self.audio_channel.play(self.MP3_Open)
				i.Global_Command()
			else:
				print('%s Команда "%s" отвечает за пояснение ~всех команд в %s' % (self.r_text_back_a, self.answer, self.r_text_back_b))
				return True
		elif self.answer.find('//') != -1 and self.answer != '//':
			if self.console_programm != 4:
				i.programm_command()
		elif self.answer == 'data' or self.answer == 'gl_data' or self.answer == 'gldata':
			if self.console_programm != 4:
				self.gl_time = localtime()
				self.time_week_day = asctime()
				i.time_mon(self.gl_time[1], self.gl_time[2], self.gl_time[3], self.gl_time[4], self.gl_time[5])
				print(self.printing_time)
				i.main_menu()
			else:
				print('%s Команда "%s" отвечает за показ времени' % (self.r_text_back_a, self.answer))
				return True
		elif self.answer == 'data_desktop' or self.answer == 'gl_data_desktop' or self.answer == 'gldata_desktop' or self.answer == 'desktop':
			if self.console_programm != 4:
				while True:
					if keyboard.is_pressed('Backspace') == True:
						while keyboard.is_pressed('Backspace') != False:
							i.Times_desktop(self.gl_time[1], self.gl_time[2], self.gl_time[3], self.gl_time[4], self.gl_time[5])
							pass
						break
					i.Times_desktop(self.gl_time[1], self.gl_time[2], self.gl_time[3], self.gl_time[4], self.gl_time[5])
				print()
				i.main_menu()
			else:
				print('%s Команда "%s" отвечает за активацию панели отдыха с анимациями' % (self.r_text_back_a, self.answer))
				return True
		elif self.answer == 'game' or self.answer == 'games':
			if self.console_programm != 4:
				print('%s Развлечения' % (self.r_text_back_a))
				i.gl_games()
			else:
				print('%s Команда "%s" отвечает за открытие игр или развлечений %s' % (self.r_text_back_a, self.answer, self.r_text_back_b))
				return True
		elif self.answer == 'settings' or self.answer == 'setin':
			if self.console_programm != 4:
				i.Settings()
			else:
				print('%s Команда "%s" отвечает за открытие настроек %s с прямым каналом' % (self.r_text_back_a, self.answer, self.r_text_back_b))
				return True
		elif self.answer == 'print' or self.answer == 'print()':
			if self.console_programm != 4:
				i.animas(n = 1, txt = '%s Что %s вы хотите вывести?:' % (self.r_text_back_a, self.pol_name))
				self.print_global_text = input('%s Что %s вы хотите вывести?: ' % (self.r_text_back_a, self.pol_name))
				print('%s %s' % (self.r_text_back_a, self.print_global_text))
				i.main_menu()
			else:
				print('%s Команда "%s" отвечает за вывод произвольного текста в консоль' % (self.r_text_back_a, self.answer))
				return True
		elif self.answer == 'clear' or self.answer == 'cls' or self.answer == 'clear_console':
			if self.console_programm != 4:
				self.clear_console()
				print('%s Произведена очистка!' % (self.r_text_back_a))
				self.global_t[3][0] = 0
				self.audio_channel.play(self.MP3_Complete)
				i.main_menu()
			else:
				print('%s Команда "%s" отвечает за очистку консоли' % (self.r_text_back_a, self.answer))
				return True
		elif self.answer == 'brower' or self.answer == 'bros':
			if self.console_programm != 4: i.brower_start()
			else:
				print('%s Команда "%s" отвечает за открытие браузера %s' % (self.r_text_back_a, self.answer, self.r_text_back_b))
				return True
		elif self.answer == 'save' or self.answer == 'saved' or self.answer.find('save') != -1:
			if self.console_programm != 4:
				i.saving_data('ALL')
				self.audio_channel.play(self.MP3_Complete)
				print('%s Данные аккаунта и системы сохранены!' % (self.r_text_back_a))
				i.main_menu()
			else:
				print('%s Команда "%s" отвечает за сохранение всех данных %s' % (self.r_text_back_a, self.answer, self.r_text_back_b))
				return True
		elif self.answer == 'ch_text' or self.answer == 'Ch_text' or self.answer == 'ch':
			if self.console_programm != 4:
				print('%s Системные изменения текста' % (self.r_text_back_a))
				i.Change()
			else:
				print('%s Команда "%s" отвечает за системные/текстовые изменения %s' % (self.r_text_back_a, self.answer, self.r_text_back_b))
				return True
		else:
			if self.console_programm != 4: i.mode_command_check()
			else:
				if i.mode_command_check() == True: return True
	def Balanse_out_account(self):
		self.position = 'balanse_out'
		print('%s %s на вашем балансе %s рублей/ %s Coin-Q' % (self.r_text_back_a, self.name, self.ruble, self.Q))
		if self.att == 0:
			self.answer = input('С какого баланса будет происходить списание? R/Q: ')
			if self.answer == 'R' or self.answer == 'r' or self.answer == 'Q' or self.answer == 'q':
				self.att += 1
				self.ans_value = self.answer
				i.Balanse_out_account()
			elif self.answer == '<' or self.answer == 'exit':
				i.animas(loading = True, txt = '%s Выход из вывода денежных средств' % (self.r_text_back_a))
				i.main_menu()
			else: i.error('0g7502')
		elif self.att == 1:
			self.answer = input('Введите сумму списания %s: ' % (self.ans_value))
			if self.answer.isnumeric() == True:
				if self.ans_value == 'R' or self.ans_value == 'r':
					if int(self.answer) <= int(self.ruble):
						self.ruble = int(self.ruble) - int(self.answer)
						self.att = 2
						i.Balanse_out_account()
				elif self.ans_value == 'Q' or self.ans_value == 'q':
					if int(self.answer) <= int(self.Q):
						self.answer = input('%s %s-Q это %s-руб. Y/N: ' % (self.r_text_back_a, self.answer, self.answer * self.coin_Q))
						if self.answer == 'Y' or self.answer == 'y':
							self.Q = int(self.Q) - int(self.answer)
							self.att = 2
							i.Balanse_out_account()
						elif self.answer == 'N' or self.answer == 'n' or self.answer == '<':
							print('%s Возвращение на одну позицию назад <-' % (self.r_text_back_a))
							self.att -= 1
							i.Balanse_out_account()
			else:
				if self.answer == '<' or self.answer == 'exit':
					print('%s Возвращение на одну позицию назад <-' % (self.r_text_back_a))
					self.att -= 1
					i.Balanse_out_account()
				else: i.error('0g7502')
		elif self.att == 2:
			if self.ans_value == 'R' or self.ans_value == 'r':
				if self.cheque == None: self.cheque = '∑/'
				else: self.cheque += '∑/'
			elif self.ans_value == 'Q' or self.ans_value == 'q':
				if self.cheque == None: self.cheque = '⨊/'
				else: self.cheque += '⨊/'
			if int(self.answer) > 100:
				if self.cheque == None: self.cheque = 'Fx+/'
				else: self.cheque += 'Fx+/'
			elif int(self.answer) < 100:
				if self.cheque == None: self.cheque = 'Fax/'
				else: self.cheque += 'Fax/'
			if self.cheque == None: self.cheque = '%s/' % (self.name)
			else: self.cheque += '%s/' % (self.name)
			if self.cheque == None: self.cheque = '%s' % (self.answer)
			else: self.cheque += '%s' % (self.answer)
			print('%s Операция прошла успешно √\n' % (self.r_text_back_a))
			if self.ans_value == 'R' or self.ans_value == 'r':
				print('----------------------------------\n%s %s\n%s Итог: %s-руб.\n----------------------------------' % (self.r_text_back_a, self.cheque, self.r_text_back_a, self.answer))
			elif self.ans_value == 'Q' or self.ans_value == 'q':
				print('----------------------------------\n%s %s\n%s Итог: %s-Q -> %s-руб.\n----------------------------------' % (self.r_text_back_a, self.cheque, self.r_text_back_a, self.answer, self.answer * self.coin_Q))
			print('\n%s Сохраните фотографию чека и отправьте разработчику в личные сообщения (Telegram: @L1s8VR9AL)\n... Укажите в сообщении номер карты, перевод произойдёт в течении 1-4 дней' % (self.r_text_back_a))
			i.main_menu()
	def Times_desktop(self, mec, day, hour, min, sec):
		self.gl_time = localtime()
		if day < 10:
			self.printing_time = '0%s.' % (self.gl_time[2])
		else:
			self.printing_time = '%s.' % (self.gl_time[2])
		if mec < 10:
			self.printing_time += '0%s.' % (self.gl_time[1])
		else:
			self.printing_time += '%s.' % (self.gl_time[1])
		self.printing_time += '%sг. /' % (self.gl_time[0])
		self.printing_time += ' %s' % (self.gl_time[3])
		if min <= 9:
			self.printing_time += ':0%s' % (self.gl_time[4])
		else:
			self.printing_time += ':%s' % (self.gl_time[4])
		if sec <= 9:
			self.printing_time += ':0%sс.' % (self.gl_time[5])
		else:
			self.printing_time += ':%sс.' % (self.gl_time[5])
	def Change(self):
		self.answer = input('Введите индекс переменной которой вы хотите изменить: ')
		if len(self.answer) == 0:
			i.Change()
		elif self.answer == '?':
			for y in range(0, len(self.r_text_name_global_var)):
				print('%s %s %s %s' % (self.r_text_back_a, self.r_text_name_global_var[y], self.r_text_back_transition, self.r_text_id_global_var[y]))
			i.Change()
		elif self.answer == 'qrtg' or self.answer == 'Qrtg' or self.answer == 'QRTG':
			self.answer = input('Вы хотите вернуть текстовые настройки к заводским? Y/N: ')
			if self.answer == 'y' or self.answer == 'Y':
				self.r_text_back_a == self.r_text_QRTG[0]
				self.r_text_back_b == self.r_text_QRTG[1]
				self.r_text_back_c == self.r_text_QRTG[2]
				self.r_text_back_transition == self.r_text_QRTG[3]
			elif self.answer == 'n' or self.answer == 'N':
				print('%s Вы отказались от сброса настроек на заводские%s' % (self.r_text_back_a, self.r_text_back_c))
				i.Change()
		elif self.answer == '<':
			i.main_menu()
		else:
			for y in range(0, len(self.r_text_name_global_var)):
				if self.answer == self.r_text_name_global_var[y] or self.answer == self.r_text_id_global_var[y]:
					self.answer = self.r_text_id_global_var[y]
					break
			if self.answer == self.r_text_id_global_var[y]:
				print('%s Начальное значение переменной "%s": "%s"' % (self.r_text_back_a, i.Change_text_print_name(self.answer), i.Change_text_print(self.answer)))
				self.r_text_answer = input('На какое значение вы хотите поменять переменную %s?: ' % (self.r_text_name_global_var[y]))
				if self.r_text_answer == '<':
					i.Change()
				else:
					i.Change_text_var(self.answer)
					print('%s Ваша переменная изменилась на: %s' % (self.r_text_back_a, self.r_text_answer))
					i.Change()
			else:
				print('%s Вы ввели неправильный индекс к переменной!' % (self.r_text_back_a))
				if self.answer.find('back') != -1:
					if self.answer.find('_a') != -1:
						print('%s Может вы имели ввиду "self.r_text_back_a"?' % (self.r_text_back_a))
					elif self.answer.find('_b') != -1:
						print('%s Может вы имели ввиду "self.r_text_back_b"?' % (self._r_text_back_а))
					elif self.answer.find('_с') != -1:
						print('%s Может вы имели ввиду "self.r_text_back_с"?' % (self._r_text_back_а))
				i.Change()
	def Change_text_var(self, id):
		if id == 'AA00001':
			self.r_text_back_a = self.r_text_answer
		elif id == 'AA00002':
			self.r_text_back_b = self.r_text_answer
		elif id == 'AA00003':
			self._r_text_back_с = self.r_text_answer
	def Change_text_print(self, id):
		if id == 'AA00001':
			return self.r_text_back_a
		elif id == 'AA00002':
			return self.r_text_back_b
		elif id == 'AA00003':
			return self._r_text_back_с
	def Change_text_print_name(self, id):
		for self.x in self.r_text_id_global_var:
			if self.answer == self.x:
				return self.answer
		return '???'
	def Settings(self): # Настройки QRTG
		self.position = 'settings'
		print('%s Настройки %s\n%s Нажмите "Ctrl + Tab" для информации' % (self.r_text_back_a, self.r_text_back_b, self.r_text_back_a))
		self.att = 0
		self.print_global_text = '%s .   ' % (self.r_text_back_a)
		while keyboard.is_pressed('Enter') != False:
			pass
		while True:
			if keyboard.is_pressed('F12') == True:
				self.att = 0
				self.print_global_text = '%s activate "F12"%s' % (self.r_text_back_a, self.loading_default[self.att])
				print('\r%s' % (self.print_global_text), end = " ")
				sleep(0.05)
				while keyboard.is_pressed('F12') != False:
					if self.activate_magic_loading == False:
						if self.att != len(self.loading_default):
							self.att += 1
							self.print_global_text = '%s activate "F12"%s' % (self.r_text_back_a, self.loading_default[self.att - 1])
						else:
							self.att = 0
							self.print_global_text = '%s activate "F12"%s' % (self.r_text_back_a, self.loading_default[self.att])
					else:
						if self.att == len(self.Magic_loading):
							self.att = 0
						else:
							self.att += 1
						self.print_global_text = '%s activate "F12"%s%s.' % (self.r_text_back_a, self.Magic_loading[self.att], self.Magic_loading2[self.att])
					print('\r%s' % (self.print_global_text), end = " ")
					sleep(0.05)
					pass
				if self.settings_master == False:
					self.settings_master = True
					print('\n%s Активация дополнительных настроек - ветка "master" √' % (self.r_text_back_a))
				else:
					self.settings_master = False
					print('\n%s Дизактивация дополнительных настроек - ветки "master" !' % (self.r_text_back_a))
			if keyboard.is_pressed('F1') == True:
				if self.settings_master == True:
					self.att = 0
					self.print_global_text = '%s activate "F1"%s' % (self.r_text_back_a, self.loading_default[self.att])
					print('\r%s' % (self.print_global_text), end = " ")
					sleep(0.05)
					while keyboard.is_pressed('F1') != False:
						if self.activate_magic_loading == False:
							if self.att != len(self.loading_default):
								self.att += 1
								self.print_global_text = '%s activate "F1"%s' % (self.r_text_back_a, self.loading_default[self.att - 1])
							else:
								self.att = 0
								self.print_global_text = '%s activate "F1"%s' % (self.r_text_back_a, self.loading_default[self.att])
						else:
							if self.att == len(self.Magic_loading):
								self.att = 0
							else:
								self.att += 1
							self.print_global_text = '%s activate "F1"%s%s.' % (self.r_text_back_a, self.Magic_loading[self.att], self.Magic_loading2[self.att])
						print('\r%s' % (self.print_global_text), end = " ")
						sleep(0.05)
						pass
					if self.developer_mode == False:
						self.developer_mode = True
						print('\n%s Активация режима разработчика √' % (self.r_text_back_a))
					else:
						self.developer_mode = False
						print('\n%s Дизактивация режима разработчика !' % (self.r_text_back_a))
			if keyboard.is_pressed('Ctrl + Alt + S') == True:
				if self.settings_master == True:
					self.att = 0
					self.print_global_text = '%s activate "Ctrl + Alt + S"%s' % (self.r_text_back_a, self.loading_default[self.att])
					print('\r%s' % (self.print_global_text), end = " ")
					sleep(0.05)
					while keyboard.is_pressed('Ctrl + Alt + S') != False:
						if self.activate_magic_loading == False:
							if self.att != len(self.loading_default):
								self.att += 1
								self.print_global_text = '%s activate "Ctrl + Alt + S"%s' % (self.r_text_back_a, self.loading_default[self.att - 1])
							else:
								self.att = 0
								self.print_global_text = '%s activate "Ctrl + Alt + S"%s' % (self.r_text_back_a, self.loading_default[self.att])
						else:
							if self.att == len(self.Magic_loading):
								self.att = 0
							else:
								self.att += 1
							self.print_global_text = '%s activate "Ctrl + Alt + S"%s%s.' % (self.r_text_back_a, self.Magic_loading[self.att], self.Magic_loading2[self.att])
						print('\r%s' % (self.print_global_text), end = " ")
						sleep(0.05)
						pass
					if self.save_data_all == False:
						self.save_data_all = True
						print('\n%s Активация мнгновенных сохранений √' % (self.r_text_back_a))
					else:
						self.save_data_all = False
						print('\n%s Дизактивация мнгновенных сохранений !' % (self.r_text_back_a))
			if keyboard.is_pressed('Ctrl + Shift + Alt + F11') == True:
				if self.settings_master == True:
					self.att = 0
					self.print_global_text = '%s activate "Ctrl + Shift + Alt + F11"%s' % (self.r_text_back_a, self.loading_default[self.att])
					print('\r%s' % (self.print_global_text), end = " ")
					sleep(0.05)
					while keyboard.is_pressed('Ctrl + Shift + Alt + F11') != False:
						if self.activate_magic_loading == False:
							if self.att != len(self.loading_default):
								self.att += 1
								self.print_global_text = '%s activate "Ctrl + Shift + Alt + F11"%s' % (self.r_text_back_a, self.loading_default[self.att - 1])
							else:
								self.att = 0
								self.print_global_text = '%s activate "Ctrl + Shift + Alt + F11"%s' % (self.r_text_back_a, self.loading_default[self.att])
						else:
							if self.att == len(self.Magic_loading):
								self.att = 0
							else:
								self.att += 1
							self.print_global_text = '%s activate "Ctrl + Shift + Alt + F11"%s%s.' % (self.r_text_back_a, self.Magic_loading[self.att], self.Magic_loading2[self.att])
						print('\r%s' % (self.print_global_text), end = " ")
						sleep(0.05)
						pass
					if self.activate_magic_loading == False:
						self.activate_magic_loading = True
						print('\n%s Активация могической загрузки √' % (self.r_text_back_a))
					else:
						self.activate_magic_loading = False
						print('\n%s Дизактивация могической загрузки !' % (self.r_text_back_a))
			if keyboard.is_pressed('Ctrl + Tab') == True:
				self.att = 0
				self.print_global_text = '%s activate "Ctrl + Tab"%s' % (self.r_text_back_a, self.loading_default[self.att])
				print('\r%s' % (self.print_global_text), end = " ")
				sleep(0.05)
				while keyboard.is_pressed('Ctrl + Tab') != False:
					if self.activate_magic_loading == False:
						if self.att != len(self.loading_default):
							self.att += 1
							self.print_global_text = '%s activate "Ctrl + Tab"%s' % (self.r_text_back_a, self.loading_default[self.att - 1])
						else:
							self.att = 0
							self.print_global_text = '%s activate "Ctrl + Tab"%s' % (self.r_text_back_a, self.loading_default[self.att])
					else:
						if self.att == len(self.Magic_loading):
							self.att = 0
						else:
							self.att += 1
						self.print_global_text = '%s activate "Ctrl + Tab"%s%s.' % (self.r_text_back_a, self.Magic_loading[self.att], self.Magic_loading2[self.att])
					print('\r%s' % (self.print_global_text), end = " ")
					sleep(0.05)
					pass
				print('\n', end = "")
				print('... "@" - Активируется даже не в настройках %s' % (self.r_text_back_b))
				print('... "Alt + Up" - Повышение громкости звуков QRTG при зажатии до 100%')
				print('... "Alt + Down" - Понижение громкости звуков QRTG при зажатии до 0%')
				print('... "Ctrl + Alt + Up" - Повышение громкости фоновой музыки при зажатии до 100% @')
				print('... "Ctrl + Alt + Down" - Понижение громкости фоновой музыки при зажатии до 0% @')
				print('... "Ctrl + Alt + Left" - Предыдущая композиция фоновой музыки @')
				print('... "Ctrl + Alt + Right" - Следующая композиция фоновой музыки @')
				print('... "Alt + F9" - Включение фоновой музыки')
				print('... "Alt + F10" - Выключение фоновой музыки')
				print('... "F12" - Дополнительные настройки')
				print('... "Backspace" - Вернуться в главное меню')
				if self.settings_master == True:
					print('... "F1" - Подключение/Отключение режима разработчика "//"')
					print('... "Ctrl + Alt + S" - Подключение/Отключение мнгновенных сохранений')
					print('... "Ctrl + Shift + Alt + F11" - Подключение/Отключение могической загрузки')
			elif keyboard.is_pressed('Alt + Up') == True and keyboard.is_pressed('Ctrl') != True:
				if not self.audio_vol >= 1:
					self.audio_vol += 0.01
					self.audio_channel.set_volume(self.audio_vol)
				self.print_global_text = '%s activate "Alt + Up"(%s) ↑' % (self.r_text_back_a, round(self.audio_vol * 100))
				self.audio_channel.set_volume(self.audio_vol)
				print('\r%s' % (self.print_global_text), end = " ")
				sleep(0.1)
				while keyboard.is_pressed('Alt + Up') != False:
					if not self.audio_vol >= 1:
						self.audio_vol += 0.01
						self.audio_channel.set_volume(self.audio_vol)
					self.print_global_text = '%s activate "Alt + Up"(%s) ↑' % (self.r_text_back_a, round(self.audio_vol * 100))
					print('\r%s' % (self.print_global_text), end = " ")
					sleep(0.1)
					pass
				i.save_setin('0_4.viu')
			elif keyboard.is_pressed('Alt + Down') == True and keyboard.is_pressed('Ctrl') != True:
				if not self.audio_vol <= 0:
					self.audio_vol -= 0.01
					self.audio_channel.set_volume(self.audio_vol)
				self.print_global_text = '%s activate "Alt + Down"(%s) ↓' % (self.r_text_back_a, round(self.audio_vol * 100))
				self.audio_channel.set_volume(self.audio_vol)
				print('\r%s' % (self.print_global_text), end = " ")
				sleep(0.1)
				while keyboard.is_pressed('Alt + Down') != False:
					if not self.audio_vol <= 0:
						self.audio_vol -= 0.01
						self.audio_channel.set_volume(self.audio_vol)
					self.print_global_text = '%s activate "Alt + Down"(%s) ↓' % (self.r_text_back_a, round(self.audio_vol * 100))
					print('\r%s' % (self.print_global_text), end = " ")
					sleep(0.1)
					pass
				i.save_setin('0_4.viu')
			elif keyboard.is_pressed('Backspace') == True:
				self.att = 0
				self.print_global_text = '%s activate "Backspace"%s' % (self.r_text_back_a, self.loading_default[self.att])
				print('\r%s' % (self.print_global_text), end = " ")
				sleep(0.05)
				while keyboard.is_pressed('Backspace') != False:
					if self.activate_magic_loading == False:
						if self.att != len(self.loading_default):
							self.att += 1
							self.print_global_text = '%s activate "Backspace"%s' % (self.r_text_back_a, self.loading_default[self.att - 1])
						else:
							self.att = 0
							self.print_global_text = '%s activate "Backspace"%s' % (self.r_text_back_a, self.loading_default[self.att])
					else:
						if self.att == len(self.Magic_loading):
							self.att = 0
						else:
							self.att += 1
						self.print_global_text = '%s activate "Backspace"%s%s.' % (self.r_text_back_a, self.Magic_loading[self.att], self.Magic_loading2[self.att])
					print('\r%s' % (self.print_global_text), end = " ")
					sleep(0.05)
					pass
				print('\n', end = "")
				if self.settings_master == True:
					print('%s Выход из режима "master"!' % (self.r_text_back_a))
					self.settings_master = False
				print('%s Настройки сохранены!' % (self.r_text_back_a))
				if self.save_data_all == True:
					i.saving_data('ALL')
				sys.stdout.flush()
				break
			elif keyboard.is_pressed('Alt + F10') == True and keyboard.is_pressed('Ctrl') != True:
				self.att = 0
				self.print_global_text = '%s activate "Alt + F10"%s' % (self.r_text_back_a, self.loading_default[self.att])
				print('\r%s' % (self.print_global_text), end = " ")
				sleep(0.05)
				while keyboard.is_pressed('Alt + F10') != False:
					if self.activate_magic_loading == False:
						if self.att != len(self.loading_default):
							self.att += 1
							self.print_global_text = '%s activate "Alt + F10"%s' % (self.r_text_back_a, self.loading_default[self.att - 1])
						else:
							self.att = 0
							self.print_global_text = '%s activate "Alt + F10"%s' % (self.r_text_back_a, self.loading_default[self.att])
					else:
						if self.att == len(self.Magic_loading):
							self.att = 0
						else:
							self.att += 1
						self.print_global_text = '%s activate "Alt + F10"%s%s.' % (self.r_text_back_a, self.Magic_loading[self.att], self.Magic_loading2[self.att])
					print('\r%s' % (self.print_global_text), end = " ")
					sleep(0.05)
					pass
				print('\n', end = "")
				if self.chill_change_return == 1:
					self.file = open('%s/TF/ClosepanelQRTG.tf' % (self.dir_python_file), 'w')
					self.file.close()
					print('Подождите...')
					sleep(1.5)
					print('... Фоновая музыка выкл.')
					self.chill_change.kill()
					self.chill_change_return = 0
				else:
					print('... Фоновая музыка уже выкл.')
			elif keyboard.is_pressed('Alt + F9') == True and keyboard.is_pressed('Ctrl') != True:
				self.att = 0
				self.print_global_text = '%s activate "Alt + F9"%s' % (self.r_text_back_a, self.loading_default[self.att])
				print('\r%s' % (self.print_global_text), end = " ")
				sleep(0.05)
				while keyboard.is_pressed('Alt + F9') != False:
					if self.activate_magic_loading == False:
						if self.att != len(self.loading_default):
							self.att += 1
							self.print_global_text = '%s activate "Alt + F9"%s' % (self.r_text_back_a, self.loading_default[self.att - 1])
						else:
							self.att = 0
							self.print_global_text = '%s activate "Alt + F9"%s' % (self.r_text_back_a, self.loading_default[self.att])
					else:
						if self.att == len(self.Magic_loading):
							self.att = 0
						else:
							self.att += 1
						self.print_global_text = '%s activate "Alt + F9"%s%s.' % (self.r_text_back_a, self.Magic_loading[self.att], self.Magic_loading2[self.att])
					print('\r%s' % (self.print_global_text), end = " ")
					sleep(0.05)
					pass
				print('\n', end = "")
				if self.chill_change_return == 0:
					self.chill_change = subprocess.Popen([sys.executable, 'Chill_change.py'])
					print('... Фоновая музыка вкл.')
					self.chill_change_return = 1
				else:
					print('... Фоновая музыка уже вкл.')
			elif keyboard.is_pressed('Ctrl + Alt + Right') == True:
				self.att = 0
				self.print_global_text = '%s activate "Ctrl + Alt + Right"%s' % (self.r_text_back_a, self.loading_default[self.att])
				print('\r%s' % (self.print_global_text), end = " ")
				sleep(0.05)
				while keyboard.is_pressed('Ctrl + Alt + Right') != False:
					if self.activate_magic_loading == False:
						if self.att != len(self.loading_default):
							self.att += 1
							self.print_global_text = '%s activate "Ctrl + Alt + Right"%s' % (self.r_text_back_a, self.loading_default[self.att - 1])
						else:
							self.att = 0
							self.print_global_text = '%s activate "Ctrl + Alt + Right"%s' % (self.r_text_back_a, self.loading_default[self.att])
					else:
						if self.att == len(self.Magic_loading):
							self.att = 0
						else:
							self.att += 1
						self.print_global_text = '%s activate "Ctrl + Alt + Right"%s%s.' % (self.r_text_back_a, self.Magic_loading[self.att], self.Magic_loading2[self.att])
					print('\r%s' % (self.print_global_text), end = " ")
					sleep(0.05)
					pass
				print('\n', end = "")
				if self.chill_change_return == 1:
					print('... Следующая композиция')
				else:
					print('... Музыка выключена - не получилось переключить композицию')
			else:
				if self.activate_magic_loading == False:
					if self.att != len(self.loading_default):
						self.att += 1
						if self.settings_master == False:
							self.print_global_text = '%s %s' % (self.r_text_back_a, self.loading_default[self.att - 1])
						else:
							self.print_global_text = '(master) %s %s' % (self.r_text_back_a, self.loading_default[self.att - 1])
					else:
						self.att = 0
						if self.settings_master == False:
							self.print_global_text = '%s %s' % (self.r_text_back_a, self.loading_default[self.att])
						else:
							self.print_global_text = '(master) %s    ' % (self.r_text_back_a)
				else:
					if self.att == len(self.Magic_loading) - 1:
						self.att = 0
					else:
						self.att += 1
					if self.settings_master == False:
						self.print_global_text = '%s %s%s ' % (self.r_text_back_a, self.Magic_loading[self.att], self.Magic_loading2[self.att])
					else:
						self.print_global_text = '(master) %s %s%s ' % (self.r_text_back_a, self.Magic_loading[self.att], self.Magic_loading2[self.att])
				print('\r%s' % (self.print_global_text), end = " ")
				sleep(0.05)
		i.main_menu()
	def save_setin(self, name_setin = None):
		if name_setin == None:
			if self.developer_mode == True:
				print('Save_setin: fun! - name_setin=None')
		elif name_setin == '0_4.viu':
			file = open('%s/Viu/0_4.viu' % (self.dir_python_file))
			self.txt, self.txting = None, ''
			while self.txt != ';':
				self.txt = file.read(1)
			while self.txt != '!':
				self.txt = file.read(1)
				self.txting += self.txt
			file.close()
			file = open('%s/Viu/0_4.viu' % (self.dir_python_file), 'w')
			file.write('{%s;%s' % (self.audio_vol, self.txting))
			if self.developer_mode == True:
				print('{%s;%s' % (self.audio_vol, self.txting))
			file.close()
			self.audio_channel.play(self.MP3_Test_volume)
			print('\n', end = "")
	def gl_games(self): # Центр развлечений
		self.position = 'game'
		self.answer = input('Строка развлечений: ')
		i.iF_gl_games()
	def iF_gl_games(self):
		if len(self.answer) == 0:
			i.gl_games()
		elif self.answer == 'Plenty' or self.answer == 'plenty':
			if self.console_programm != 4:
				self.position = 'game_play'
				i.Games_for_3N_1()
			else:
				print('%s Игра-команда "%s" отвечает за открытие логической игры с числами 3n+1' % (self.r_text_back_a, self.answer))
				return True
		elif self.answer == '<' or self.answer == 'exit':
			if self.console_programm != 4:
				i.main_menu()
			else:
				print('%s "%s" отвечает за выход из ~всех консолей назад' % (self.r_text_back_a, self.answer))
				return True
		else:
			if self.console_programm != 4:
				i.error('0g7502')
	def Games_for_3N_1(self): # Игра "plenty"
		self.N = input('Введите любое положительное число: ')
		self.answer = self.N
		if self.N.isnumeric() == True:
			self.N = int(self.N)
			if not self.N <= 0:
				while True:
					if self.N == 1: break
					if self.N % 2 == 0: self.N = int(self.N / 2)
					elif int(self.N) % 2 == 1: self.N = int(3 * self.N + 1)
					self.att += 1
					print(' '*20,end='')
					print('\r%s Число: %sn%s Попытка: %s' % (self.r_text_back_a, self.N, self.r_text_back_a, self.att), end = '')
					sleep(0.1)
				print('\n%s Число: %s прошло до 1 за %s комбинаций' % (self.r_text_back_a, self.answer, self.att))
				self.att = 0
				i.Games_for_3N_1()
			else:
				print('%s Такое число не принимает бесконечный цикл 3n+1' % (self.r_text_back_a))
				self.audio_channel.play(self.MP3_Denial)
				i.Games_for_3N_1()
		else:
			if self.answer == '<' or self.answer == 'back' or self.answer == 'exit':
				i.gl_games()
			else:
				i.error('0g7502')
	def programm_command(self): # Проверка быстрого ввода команды - переключения
		if self.developer_mode == True:
			if self.answer == '//m':
				print(self.console_mode_activate)
				self.console_programm = 2
				if self.console_mode_activate == False or self.console_mode_activate == 'False':
					self.console_mode_activate = True
					i.read_modepacks()
				elif self.console_mode_activate == True or self.console_mode_activate == 'True':
					print('%s Отказано в доступе' % (self.r_text_back_a))
					self.audio_channel.play(self.MP3_Denial)
					i.main_menu()
			elif self.answer == '//i':
				print(self.console_mode_activate)
				self.console_programm = 2
				if self.console_mode_activate == True or self.console_mode_activate == 'True':
					self.position = 'import_mode'
					i.console_mode()
				elif self.console_mode_activate == False or self.console_mode_activate == 'False':
					print('%s Отказано в доступе' % (self.r_text_back_a))
					self.audio_channel.play(self.MP3_Denial)
					i.main_menu()
			elif self.answer == '//?':
				print('//m //i //?')
				i.main_menu()
			else:
				i.error('0g7503')
		else:
			i.error('0g7503')
	def Global_Command(self): # Пояснение ~всех команд клиента
		self.exit_gl_command = 0
		self.ipp = None
		self.answer = input('Введите команду которую хотите проверить: ')
		self.console_programm = 4
		if len(self.answer) == 0:
			self.console_programm = 0
			self.exit_gl_command = 1
			self.audio_channel.play(self.MP3_Off)
			i.main_menu()
		elif i.iF_main_menu() != True and i.iF_gl_games() != True:
			self.exit_gl_command = 0
			self.audio_channel.play(self.MP3_Warning)
			print('%s Такой команды нет или я пока что её не знаю...' % (self.r_text_back_a))
		if self.exit_gl_command == 0:
			i.Global_Command()
	def coin_pr(self, activate_menu = True, c = 0): # Проверка изменение стоимости валют в бирже
		self.global_t[c][1] = time()
		self.global_t[c][2] = (self.global_t[c][1]-self.global_t[c][0]) // 300
		if self.global_t[c][2] >= 1:
			s = randint(-80, 80)
			if s <= 0:
				if c == 0:
					if self.coin_Q - s > 0:
						self.coin_Q -= abs(s)
				elif c == 1:
					if self.coin_ruble - s > 0:
						self.coin_ruble -= abs(s)
			else:
				if c == 0:
					self.coin_Q += s
				else:
					self.coin_ruble += s
			self.global_t[c][0] = time()
		if self.coin_ruble_Q_pos == False:
			i.animas(loading = True, txt = '%s Открытие биржи' % (self.r_text_back_a))
			if self.developer_mode == True:
				print(self.coin_Q)
				print(self.active_coin_Q)
				print(self.coin_ruble)
				print(self.active_coin_ruble)
				print(self.ruble)
				print(self.Q)
		elif self.coin_ruble_Q_pos == True:
			self.coin_ruble_Q_pos = False
		if activate_menu == True:
			if self.active_coin_ruble == True:
				i.coin_pr(activate_menu = False, c = 1)
				i.coin()
	def coin(self, price_vision = None): # Строка биржи
		self.position, self.ifip = 'coin_Q', 0
		if randint(0,1) == 1 or price_vision == True:
			i.animas(txt = '%s 1qC = %s рублей' % (self.r_text_back_a, self.coin_Q))
		i.animas(n = 1, txt = 'Строка биржи:')
		self.answer = input('Строка биржи: ')
		if self.active_coin_Q == True:
			self.global_t[0][2] = (self.global_t[0][1]-self.global_t[0][0]) // 300
			if self.global_t[0][2] >= 1: i.iF_coin_Q(True)
			else: i.iF_coin_Q(False)
		elif self.active_coin_Q == False: i.iF_coin_Q(False)
	def iF_coin_Q(self, variability): # Проверка команды в бирже
		if variability == True:
			i.animas(loading = True, txt = '%s Продажа qC изменилась, требуется перезагрузка биржи' % (self.r_text_back_a))
			self.coin_ruble_Q_pos = True
			self.audio_channel.play(self.MP3_Warning)
			self.pre_coin_Q = self.coin_Q
			i.coin_pr(False), i.iF_coin_Q(False)
		elif variability == False:
			if self.answer == '<' or\
			self.answer == 'exit':
				self.audio_channel.play(self.MP3_Off)
				i.animas(loading = True, txt = '%s Выход из биржи' % (self.r_text_back_a))
				i.main_menu()
			elif len(self.answer) == 0: i.coin()
			elif self.answer == 'Q' or self.answer == 'q' or self.answer == 'R' or self.answer == 'r':
				if self.answer == 'R' or self.answer == 'r': symrel = 'рублей'
				elif self.answer == 'Q' or self.answer == 'q': symrel = 'qC'
				print('%s %s, в вашей копилке %s %s' % (self.r_text_back_a, self.name, self.Q, symrel))
				i.coin()
			elif self.answer == 'bank': i.bank()
			elif self.answer == 'piggy':
				print('%s %s, в вашей копилке %s рублей и %s qC' % (self.r_text_back_a, self.name, self.ruble, self.Q))
				i.coin()
			elif self.answer == 'price': i.coin(True)
			elif self.answer == 'rate': i.rate_pr()
			else: i.mode_command_check()
		else:
			i.error('0g7503')
	def rate_pr(self): # Проверка ставок
		print('%s Проверка обновления ставок...' % (self.r_text_back_a))
		sleep(0.2)
		if self.rate_update != 1:
			self.global_t[2][2] = (self.global_t[2][0] - self.global_t[2][1]) // 300
		else:
			self.global_t[2][2] = 1
			self.rate_update = 0
		self.global_t[2][1] = time()
		if self.global_t[2][2] >= 1:
			print('%s Обновление ставок...' % (self.r_text_back_a))
			sleep(0.6)
			self.rate_name = []
			self.rate_price = []
			self.rate_price_coin = []
			self.rate_profit = []
			self.rate_profit_coin = []
			for y2 in range(0, 10):
				if self.developer_mode == True:
					print('y2 = %s' % (y2))
				self.rate_random_number = randint(0, len(self.rate_random_name) - 1)
				if len(self.rate_name) != 0:
					while True:
						for y in range(len(self.rate_name)):
							if self.developer_mode == True:
								print('y+ = %s\n y = %s' % (len(self.rate_name), y))
								print(self.rate_name[y])
								print('%s\n' % (self.rate_random_name[self.rate_random_number]))
								sleep(0.3)
							if self.rate_name[y] == self.rate_random_name[self.rate_random_number]:
								self.rate_random_number = randint(0, len(self.rate_random_name) - 1)
								self.rate_equally_name = True
								break
						if self.rate_equally_name != True:
							break
						elif self.rate_equally_name == True:
							self.rate_equally_name = False
					self.rate_name.append(self.rate_random_name[self.rate_random_number])
					self.rate_equally_name = None
				elif len(self.rate_name) == 0:
					self.rate_name.append(self.rate_random_name[self.rate_random_number])
				self.rate_random_number = randint(0, 1)
				if self.rate_random_number == 0:
					self.rate_price_coin.append('ruble')
					self.rate_random_number = randint(self.coin_Q - 15, self.coin_Q + 40)
				elif self.rate_random_number == 1:
					self.rate_price_coin.append('qC')
					self.rate_random_number = randint(self.coin_Q // self.coin_Q, self.coin_Q * 230 // self.coin_Q)
				self.rate_price.append(self.rate_random_number)
				self.rate_len = len(self.rate_price) - 1
				self.rate_random_number = randint(0, 1)
				if self.rate_random_number == 0:
					self.rate_profit_coin.append('ruble')
					if self.rate_price_coin[self.rate_len] == 'ruble':
						self.rate_random_number = randint(self.coin_Q - 25, self.coin_Q + 45)
					elif self.rate_price_coin[self.rate_len] == 'qC':
						self.rate_random_number = randint((int(self.rate_price[self.rate_len]) * self.coin_Q) - 2, (int(self.rate_price[self.rate_len]) * self.coin_Q) + 5)
				elif self.rate_random_number == 1:
					self.rate_profit_coin.append('qC')
					if self.rate_price_coin[self.rate_len] == 'ruble':
						self.rate_random_number = randint((int(self.rate_price[self.rate_len]) // self.coin_Q) + 1, (int(self.rate_price[self.rate_len]) // self.coin_Q) + 3)
					elif self.rate_price_coin[self.rate_len] == 'qC':
						self.rate_random_number = randint(self.coin_Q // self.coin_Q + (int(self.rate_price[self.rate_len]) - 2), self.coin_Q // self.coin_Q + (int(self.rate_price[self.rate_len]) + 5))
				self.rate_profit.append(self.rate_random_number)
			self.global_t[2][0] = time()
		else:
			print('%s Начальные ставки актуальны...' % (self.r_text_back_a))
		for y in range(0, 10):
			i.animas( txt = '%s. "%s" продаёт %s%s за %s%s' % (y + 1, self.rate_name[y], self.rate_price[y], self.rate_price_coin[y], self.rate_profit[y], self.rate_profit_coin[y]))
		i.rate_global()
	def rate_global(self):
		self.position, self.rate_ipp = 'rate', 0
		self.answer = input('Строка ставок: ')
		i.iF_rate_global()
	def iF_rate_global(self): # Проверка команды в разделе биржи "Ставки"
		if self.rate_ipp == 0:
			if len(self.answer) == 0: i.rate_global()
			elif self.answer == 'buy': i.rate_buy()
			elif self.answer == 'update' or self.answer == 'Update': self.rate_update = 1, i.rate_pr()
			elif self.answer == '<' or self.answer == 'exit':
				print('%s Строка биржи' % (self.r_text_back_a))
				i.coin()
			else: i.error('0g7502')
		elif self.rate_ipp == 1:
			self.if_for_global = False
			for y in range(0, 10):
				if self.developer_mode == True:
					print(self.rate_name[y])
					print(self.answer)
				if self.answer == self.rate_name[y]:
					if self.developer_mode == True:
						print('+')
						print(self.rate_price_coin[y])
					self.if_for_global = True
					if self.rate_price_coin[y] == 'qC':
						if int(self.rate_price[y]) <= int(self.Q):
							if self.developer_mode == True:
								print(int(self.rate_price[y]))
								print(int(self.rate_profit[y]))
								print('%s Q = %s' % (self.r_text_back_a, int(self.Q)))
							self.Q = int(self.Q) + int(self.rate_price[y])
							if self.rate_profit_coin[y] == 'qC':
								self.Q = int(self.Q) - int(self.rate_profit[y])
							elif self.rate_profit_coin[y] == 'ruble':
								self.ruble = int(self.ruble) - int(self.rate_profit[y])
							print('%s Сделка прошла успешно...\n%s Вы купили %s%s за %s%s' % (self.r_text_back_a, self.r_text_back_a, self.rate_price[y], self.rate_price_coin[y], self.rate_profit[y],\
							self.rate_profit_coin[y]))
						elif int(self.rate_price[y]) > int(self.Q):
							print('%s У вас %s недостаточно средств "%s%s" для совершения операции покупки...' % (self.r_text_back_a, self.pol_name, self.Q, self.rate_profit_coin[y]))
						i.rate_pr()
					elif self.rate_price_coin[y] == 'ruble':
						if int(self.rate_price[y]) <= int(self.ruble):
							if self.developer_mode == True:
								print(int(self.rate_price[y]))
								print(int(self.rate_profit[y]))
								print('%s ruble = %s' % (self.r_text_back_a, int(self.ruble)))
							self.ruble = int(self.ruble) + int(self.rate_price[y])
							if self.rate_profit_coin[y] == 'qC':
								self.Q = int(self.Q) - int(self.rate_profit[y])
							elif self.rate_profit_coin[y] == 'ruble':
								self.ruble = int(self.ruble) - int(self.rate_profit[y])
							print('%s Сделка прошла успешно...\n%s Вы купили %s%s за %s%s' % (self.r_text_back_a, self.r_text_back_a, self.rate_price[y], self.rate_price_coin[y], self.rate_profit[y],\
							self.rate_profit_coin[y]))
						elif int(self.rate_price[y]) > int(self.ruble):
							print('%s У вас %s недостаточно средств "%s%s" для совершения операции покупки...' % (self.r_text_back_a, self.pol_name, self.ruble, self.rate_profit_coin[y]))
						i.rate_pr()
			if self.if_for_global == False:
				print('%s Мне не удалось найти совпадающие имена...' % (self.r_text_back_a))
				self.audio_channel.play(self.MP3_Denial)
				i.rate_pr()
	def rate_buy(self): # Создание сделки в ставках
		print('%s Чью ставку вы %s хотите купить?\n%s (Введите имя)' % (self.r_text_back_a, self.pol_name, self.r_text_back_a))
		print('%s Ставки:' % (self.r_text_back_a))
		for y in range(0, 10):
			print('%s. "%s"' % (y + 1, self.rate_name[y]))
		self.answer = input('Оформление сделки с : ')
		self.rate_ipp = 1
		i.iF_rate_global()
	def bank(self): # Банк биржи
		self.ipp = None
		self.position = 'bank_b0'
		if self.ifip == 0:
			print('%s Банк' % (self.r_text_back_a))
			print('%s %s вы перешли в отделение банка №1' % (self.r_text_back_a, self.pol_name))
		self.answer = input('Строка банка: ')
		self.x = 0
		i.iF_bank(0)
	def iF_bank(self, b_ans): # Проверка команды в банке (под определённым разделом)
		if b_ans == 0:
			if len(self.answer) == 0:
				self.ifip = 1
				i.bank()
			elif self.answer == 'ruble' or\
			self.answer == 'r' or self.answer == 'rub':
				if self.active_coin_Q == True:
					print('%s %s, ставка на обмен q-монет: 1qC = %sруб. -> %sруб.\n%s Банк' % (self.r_text_back_a, self.name, self.pre_coin_Q, self.coin_Q, self.r_text_back_a))
				elif self.active_coin_Q == False:
					print('%s %s, ставка на обмен q-монет: 1qC = %sруб. \n%s Банк' % (self.r_text_back_a, self.name, self.coin_Q, self.r_text_back_a))
				self.ifip = 1
				i.bank()
			elif self.answer == 'qC' or\
			self.answer == 'q' or\
			self.answer == 'coin_Q' or\
			self.answer == 'Q':
				if self.active_coin_ruble == True:
					print('%s %s, ставка на обмен рублей: %sруб. -> %sруб. = 1qC\n%s Банк' % (self_r_text_back_a, self.name, self.pre_coin_Q, self.coin_Q, self.r_text_back_a))
				elif self.active_coin_ruble == False:
					print('%s %s, ставка на обмен рублей: %sруб. = 1qC\n%s Банк' % (self.r_text_back_a, self.name, self.coin_Q, self.r_text_back_a))
				self.ifip = 1
				i.bank()
			elif self.answer == 'buy':
				self.ifip = 0
				i.buy_vaule()
			elif self.answer == '<' or\
			self.answer == 'exit':
				self.ifip = 0
				if self.active_coin_Q == True or\
				self.active_coin_ruble == True:
					i.coin_pr(True)
				else:
					i.coin()
			elif self.answer == 'price' or self.answer == 'balanse':
				print('%s %s, в копилке %s рублей и %sqC' % (self.r_text_back_a, self.name, self.ruble, self.Q))
				self.ifip = 1
				i.bank()
			else:
				i.mode_command_check()
		elif b_ans == 1:
			self.position = 'bank_b1'
			if len(self.answer) == 0:
				self.ifip = 1
				i.buy_vaule()
			elif self.answer == 'r':
				self.val = 'r'
				i.buy_sum()
			elif self.answer == 'q':
				self.val = 'q'
				i.buy_sum()
			elif self.answer == '<' or self.answer == 'exit':
				self.audio_channel.play(self.MP3_Off)
				self.ifip = 0
				i.bank()
			else:
				i.mode_command_check()
		elif b_ans == 2:
			self.position = 'bank_b2'
			if len(self.answer) == 0:
				self.ifip = 1
				i.buy_sum_rel()
			elif self.answer == '<' or self.answer == 'exit':
				self.ifip = 0
				self.audio_channel.play(self.MP3_Off)
				i.bank()
			elif self.val == 'r':
				if int(self.Q) - int(self.answer) >= 0:
					self.ruble = int(self.ruble) + int(self.answer) * int(self.coin_Q)
					self.Q = int(self.Q) - int(self.answer)
					print('%s Обмен произошёл успешно' % (self.r_text_back_a))
					self.audio_channel.play(self.MP3_Complete)
					print(self.ruble)
					print(self.Q)
					i.bank()
				else:
					i.error('0g7506')
			elif self.val == 'q':
				if int(self.ruble) - int(self.answer) * int(self.coin_Q) >= 0:
					self.Q = int(self.Q) + int(self.answer)
					self.ruble = int(self.ruble) - int(self.answer) * int(self.coin_Q)
					self.audio_channel.play(self.MP3_Complete)
					print('%s Обмен произошёл успешно' % (self.r_text_back_a))
					print(self.ruble)
					print(self.Q)
					i.bank()
				else:
					i.error('0g7506')
			else:
				i.error('0g7502')	
	def buy_vaule(self): # Покупка или !обмен! валют
		self.ipp = None
		if self.ifip == 0:
			print('%s Какую валюту вы хотите приобрести?' % (self.r_text_back_a))
			print('%s %s вы перешли в отделение банка №2' % (self.r_text_back_a, self.pol_name))
		self.answer = input('Валюта: ')
		self.x = 0
		i.iF_bank(1)
	def buy_sum(self): # Проверка суммы обмена валют
		if self.val == 'r':
			symbel, symbel_1 = 'обменять', '1qC = %sруб.' % (self.coin_Q)
		elif self.val == 'q':
			symbel = 'получить'
		else:
			i.error('0g7502')
		if self.val == 'r' or self.val == 'q':
			print('%s Сколько %s вы хотите %s qC?' % (self.r_text_back_a, self.name, symbel))
			if self.active_coin_Q == True:
				symbel_1 = '1qC = %sруб. -> %sруб.' % (self.pre_coin_Q, self.coin_Q)
			print('%s %s, ставка на обмен: %s\n%s Банк' % (self.r_text_back_a, self.name, symrel_1, self.r_text_back_a))
			self.ifip = 0
			i.buy_sum_rel()
	def buy_sum_rel(self): # Ввод суммы обмена валютами
		self.ipp = None
		if self.ifip == 0:
			print('%s %s вы перешли в отделение банка №3' % (self.r_text_back_a, self.pol_name))
		self.answer = input('Сумма: ')
		self.x = 0
		i.iF_bank(2)
	def read_modepacks(self): # Проверка установленных модов
		self.number_pos, inporting_pov_system, self.position = 0, 0, 'read_modes'
		os.chdir('ModePack')
		for root, dirs, files in os.walk(".", topdown = True):
			for name in files:
				if name.endswith('.rct'):
					if self.developer_mode == True:
						print(self.ModeFic_global)
					if len(self.ModeFic_global[0]) != 0:
						for y in range(len(self.ModeFic_global[0])):
							if self.developer_mode == True:
								print(os.path.join(name) == self.ModeFic_global[0][y])
							if os.path.join(name) == self.ModeFic_global[0][y]:
								inporting_pov_system = 1
								break
						if inporting_pov_system != 1:
							self.ModeFic_global[0].append(os.path.join(name))
						inporting_pov_system = 0
					else:
						self.ModeFic_global[0].append(os.path.join(name))
					self.number_pos += 1
				else:
					if name.endswith('.txt'):
						self.number_pos += 1
					else:
						os.chdir('..')
						i.error('0g7503')
						break
		if self.position != 'ERROR':
			symbol = ''
			os.chdir('..')
			if self.save_data_all == True:
				i.saving_data('ALL')
			if self.number_pos > 0:
				self.audio_channel.play(self.MP3_Open)
				if len(self.ModeFic_global[0]) > 1:
					symbol = 'ы'
				if len(self.ModeFic_global[0]) != 0:
					print('...Мод%s: ' % (symbol), end='')
					for x in self.ModeFic_global[0]:
						if self.ModeFic_global[0].index(x) != len(self.ModeFic_global[0])-1: print(x, end=', ')
						else: print(x)
				else:
					print('%s Никаких модов не установлено!' % (self.r_text_back_a))
			else:
				self.audio_channel.play(self.MP3_Off)
				print('%s Моды не установлены или их нет в папке "ModePack"...' % (self.r_text_back_a))
			i.mini_function('console_end_command')
	def log_file_change(self, log_command): # LOG-команды из консоли
		if log_command == 'log_read':
			log = open('%s/log.log' % (self.dir_python_file))
			print(log.read())
			log.close()
		elif log_command == 'log_clear':
			log = open('%s/log.log' % (self.dir_python_file), 'w')
			log.write('%s [%s] Clear file' % (self.r_text_back_a, asctime()))
			log.close()
			print('%s Очистка выполнина успешно' % (self.r_text_back_a))
			self.audio_channel.play(self.MP3_Complete)
		elif log_command == 'note':
			self.answer = input('Напишите вашу заметку: ')
			if self.answer == '<' or self.answer == 'exit':
				print('%s Заметка отменена' % (self.r_text_back_a))
				self.audio_channel.play(self.MP3_Denial)
			else:
				if self.answer.find(R'\n') == -1:
					note_txt = i.mini_function('note')
					note = open('%s/note.txt' % (self.dir_python_file), 'w')
					note.write('%s\n[%s] %s Заметка %s: "%s"' % (note_txt, asctime(), self.r_text_back_a, self.pol_name, self.answer))
					print('<%s Ваша заметка записана через ярлык "Notes" в текстовый документ "note.txt"\n<%s Заметка %s: "%s"' % (self.r_text_back_a, self.r_text_back_a, self.pol_name, self.answer))
					self.audio_channel.play(self.MP3_Complete)
					note.close()
				else:
					i.error('0g7503')
		elif log_command == 'log_fake_error' or log_command == 'log_fake' or log_command == 'log_0g7505':
			log_txt = i.mini_function('log')
			log = open('%s/log.log' % (self.dir_python_file),'w')
			log.write('%s\n%s [%s] Error 0g7505: Fake error///' % (log_txt, self.r_text_back_a, asctime()))
			log.close()
			print('%s Fake error///' % (self.r_text_back_a))
			self.audio_channel.play(self.MP3_Warning)
		else: i.error('0g7503')
		if self.position != 'ERROR': i.mini_function('console_end_command')
	def mode_activate(self): # Активация команды в моде
		position_mode = self.ModeFic_global[6]
		for_num = self.ModeFic_global[4][self.x]
		begin_number = int(self.ModeFic_global[5][self.x])
		if position_mode[self.x] == self.position:
			for y in range(0,int(for_num)):
				if self.developer_mode == True:
					print('Начальный индекс: %s' % (self.x))
					print('Дополнительный индекс: %s' % (y))
					print('Сколько действий в команде:', for_num)
					print('Все начала отсчёта: %s' % (self.ModeFic_global[5]))
					print('Все названия функций для выполнения: %s' % (self.ModeFic_global[2]))
					print('Все итоги выполнения функций: %s' % (self.ModeFic_global[3]))
				log_txt = i.mini_function('log')
				Modefic_com = self.ModeFic_global[2][begin_number + y]
				Modefic_com_visual = self.ModeFic_global[3][begin_number + y]
				if len(self.ModeFic_global[9]) > 0 and 'sleep' in self.ModeFic_global[3]:
					sleep_print_mode = self.ModeFic_global[9][y]
				if len(self.ModeFic_global[10]) > 0 and 'log' in self.ModeFic_global[3]:
					log_write = self.ModeFic_global[10][y]
				if self.position != 'ERROR':
					if Modefic_com == 'print':
						print('%s %s' % (self.r_text_back_a, Modefic_com_visual))
					elif Modefic_com == 'cl':
						if Modefic_com_visual == 'console_start' or Modefic_com_visual == 'con_st': self.console_programm = 0, i.console_start()
						elif Modefic_com_visual == 'main_menu' or Modefic_com_visual == 'menu': i.main_menu()
						elif Modefic_com_visual == 'coin' or Modefic_com_visual == 'C' or Modefic_com_visual == '$': i.coin_pr(True)
						else:
							if Modefic_com_visual != '0': i.error('0g7504')
							else: i.main_menu()
					elif Modefic_com == 'log':
						log = open('%s/log.log' % (self.dir_python_file),'w')
						if Modefic_com_visual == '__fake__':
							log_text_print = '%s\n%s [%s] Error 0g7505: Fake error///' % (log_txt, self.r_text_back_a, asctime())
						elif Modefic_com_visual == '__text__':
							log_text_print = '%s\n%s' % (log_txt, log_write)
						else:
							log_text_print = '%s\n%s [%s] %s' % (log_txt, self.r_text_back_a, asctime(), Modefic_com_visual)
						print(log.write('%s' % (log_text_print)))
						log.close()
					elif Modefic_com == 'sleep':
						if sleep_print_mode == 'True':
							print('< ..sleeping.. >')
							self.audio_channel.play(self.MP3_Warning)
						elif sleep_print_mode == 'False':
							log = open('%s/log.log' % (self.dir_python_file),'w')
							log.write('%s\n%s [%s] < ..Active command "%s" and sleeping %ssec.. >' % (log_txt, self.r_text_back_a, asctime(), self.answer, Modefic_com_visual))
							log.close()
						sleep(int(Modefic_com_visual))
					else:
						i.error('0g7504')
						self.position = 'noneCOMMAND'
						break
				else:
					i.error('0g7502')
			if (self.position != 'ERROR' and Modefic_com_visual == '0' and self.re_boot != 1) or self.position == 'noneCOMMAND': i.main_menu()
		elif position_mode[self.x] != self.position: self.x += 1, i.mode_activate()
		else: i.error('0g7502')
	def saving_data(self, save):
		if self.developer_mode == True:
			print('<<><><>>')
			print(self.Q)
			print(self.ruble)
		if save == 'Data_system' or save == 'ALL':
			self.file = open('%s/Saven.dll' % (self.dir_python_file),'w')
			self.file.write('%s;%s;%s;%s;%s;%s;%s;%s;%s.' %\
			(self.pos_txt_system, self.number_pos, self.global_command_number_system, \
			self.chill_change_return, self.sleep_night, self.developer_mode, \
			self.save_data_all, self.activate_magic_loading, self.desktop_log))
			self.file.close()
		if save == 'Coin' or save == 'ALL':
			self.file = open('%s/Coin.txt' % (self.dir_python_file), 'w')
			self.file.write('%s;%s;%s;%s{%s:%s}' % (self.coin_Q, self.active_coin_Q, self.coin_ruble, self.active_coin_ruble, self.Q, self.ruble))
			self.file.close()
		if save == 'Data_mode' or save == 'ALL':
			self.file = open('%s/Saven_Mods.dll' % (self.dir_python_file), 'w')
			self.file.write('[%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s]!' % (
				self.ModeFic_global[0], self.ModeFic_global[1], self.ModeFic_global[2], self.ModeFic_global[3],\
				self.ModeFic_global[4], self.ModeFic_global[5], self.ModeFic_global[6], self.ModeFic_global[7],\
				self.ModeFic_global[8], self.ModeFic_global[9], self.ModeFic_global[10], self.ModeFic_global[11], self.ModeFic_global[12]
				))
			self.file.close()
		if save == 'Search_brower' or save == 'ALL':
			self.file = open('%s/Internet QRTG/Search.javas' % (self.dir_python_file), 'w')
			self.file.write('search{\n%s}' % (self.internet_searching))
			self.file.close()
		if save == 'Data_brower' or save == 'ALL':
			self.file = open('%s/Internet QRTG/Pall.javas' % (self.dir_python_file), 'w')
			self.file.write('\
				internet.global(T)\n\
				internet.system.F(close)\n\
				internet.portal(%s)\n\
				un.system(file)\n\
				un.system(brower)\n\
				un.coding(%s)\n\
				un.start(%s)\n\
				internet.system.T(close)'\
			% (self.internet_protocol, self.internet_coding[0], self.internet_start_str))
			self.file.close()
			if self.developer_mode == True:
				self.file = open('%s/Internet QRTG/Pall.javas' % (self.dir_python_file))
				print(self.file.read())
				self.file.close()
	def exit_file_client(self): # Выход из файла
		self.audio_channel.play(self.MP3_Warning)
		i.animas(n = 1, txt = '%s, вы хотите завершить работу?:' % (self.name))
		self.answer = input('%s, вы хотите завершить работу?: ' % (self.name))
		if self.answer == 'yes' or self.answer == '+' or self.answer == 'да':
			if self.save_data_all == False:
				i.saving_data('ALL')
			self.file = open('%s/TF/ClosepanelQRTG.tf' % (self.dir_python_file), 'w'), self.file.close()
			sleep(0.12)
			self.audio_channel.play(self.MP3_Bye_file)
			self.audio_channel.play(self.MP3_Client_byebye)
			self.exit_file = True
			i.animas(txt = '%s Завершение работы...' % (self.r_text_back_a))
			sleep(2)
			if self.chill_change_return == 1:
				self.chill_change.kill()
			sys.exit(0)
		elif self.answer == 'no' or self.answer == 'нет' or self.answer == '-':
			self.audio_channel.play(self.MP3_Complete)
			i.animas(loading = True, txt = '%s Продолжаем' % (self.r_text_back_a))
			sleep(0.9)
			i.main_menu()
		else:
			i.error('0g7503')
	pass
from sys_import import *
warnings.filterwarnings("ignore")
pygame.init()
i = II()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']), options.add_argument("--headless")
i.brower_chrome = webdriver.Chrome(chrome_options=options)# Открытие браузера
#i.brower_chrome.get('https://text-host.ru/raw/ui-75747-7')# Переход по ссылке
#txt_code = i.brower_chrome.find_element_by_css_selector("pre")# Чтение закодированного текста
#print(txt_code.text)
i.jik_read('0_1.viu', open('%s/Viu/0_1.viu' % (i.dir_python_file)))
i.jik_read('0_4.viu', open('%s/Viu/0_4.viu' % (i.dir_python_file)))
i.audio_channel.set_volume(i.audio_vol)
i.start_job()
if i.developer_mode == True:
	print('Выход из файла: ', i.exit_file)
	print('Перезагрузка: ', i.re_boot)
	sleep(1.6)
while i.exit_file != True:
	if i.re_boot == 1:
		i.file = open('%s/TF/RebootinformationpanelQRTG.tf' % (i.dir_python_file), 'w')
		i.file.write('REBOOT')
		i.file.close()
		i.__init__()
		i.start_job()