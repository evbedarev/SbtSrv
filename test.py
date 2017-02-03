
# def a_decorator_passing_arbitrary_arguments(fun_to_decorate):
# 	#all args
# 	def wrapper(*args,**kwargs):
# 		print("Передали ли мне что-нибудь?:")
# 		print(args)
# 		print(kwargs)
# 		fun_to_decorate(*args,**kwargs)
# 	return wrapper

# @a_decorator_passing_arbitrary_arguments
# def func_no_args():
# 	print("No arguments here.")

# @a_decorator_passing_arbitrary_arguments
# def func_with_args(a,b,c):
# 	print(a,b,c)

# @a_decorator_passing_arbitrary_arguments
# def func_with_slov(a,b,c,platypus="Почему нет?"):
# 	print("Любят ли {}, {} и {} утконосов? {}".format(a,b,c,platypus))

# func_with_slov("Женя","Стив","Бил",platypus="Определенно!")