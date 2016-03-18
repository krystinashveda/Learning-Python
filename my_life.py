def opportunity_check():
	opportunity = input("What opportunity do you consider? Type: tier2, job, startup, freelance OR exit to stop. ")
	if opportunity == "exit":
		exit()
	elif opportunity == "tier2":
		print("success")
		exit()
	elif opportunity == "job":
		visa_question = input("Is visa possible? Type: yes, no. ")
		if visa_question == "yes":
			print("keep goin. Come back in a month.")
			exit()
		else:
			print("Look for another opportunity")
			opportunity_check()
	elif opportunity == "startup" or "freelance":
		progress = input("Is there substantial progress, e.g. money? Type: yes, no. ")
		if progress == "yes":
			print("Keep goin. Come back in a month.")
			print ("Extend Tier 1 for 1 year")
			exit()
		else:
			print("Look for another opportunity")
			opportunity_check()
	else:
		print("Look for another opportunity")
		opportunity_check()

opportunity_check()