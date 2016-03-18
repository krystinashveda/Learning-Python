while True:
	opportunity = input("What opportunity do you consider? Type: tier2, job, startup, freelance OR exit to stop. ")
	if opportunity == "exit":
		break
	elif opportunity == "tier2":
		print("success")
		break
	elif opportunity == "job":
		visa_question = input("Is visa possible? Type: yes, no. ")
		if visa_question == "yes":
			print("Keep goin. Come back in a month.")
			break
		elif visa_question == "no":
			continue
		else:
			continue
	elif opportunity == "startup" or "freelance":
		progress = input("Is there substantial progress, e.g. money? Type: yes, no. ")
		if progress == "yes":
			print("Keep goin. Come back in a month.")
			print ("Extend Tier 1 for 1 year")
			break
		elif progress == "no":
			continue
		else:
			continue
	else:
			continue





