from sys import exit
import time
import threading

free_messages = 3
timeout = None
current_language = 'en' 

def ask_question(question):
    global timeout
    print(question, end='')
    
    def terminate():
        print('HMI terminated.')
        exit()

    timeout = threading.Timer(15, terminate)
    timeout.start()
    
    answer = input().strip()
    timeout.cancel()
    return answer

def ussd_menu(show_back=False):
    global free_messages, current_language
    if current_language == 'en':
        menu_text = (
            "Menu USSD:\n"
            + ("0. Back\n" if show_back else "")
            + "1. Mobile Money\n"
            + "2. Buy a plan\n"
            + "3. Send a free message\n"
            + "4. Call Me Back\n"
            + "5. Language\n"
            + "Choose option: "
        )
    else:  
        menu_text = (
            "Menu USSD:\n"
            + ("0. Retour\n" if show_back else "")
            + "1. Argent Mobile\n"
            + "2. Acheter un plan\n"
            + "3. Envoyer un message gratuit\n"
            + "4. Rappelle-moi\n"
            + "5. Langue\n"
            + "Choisissez une option: "
        )
    
    option = ask_question(menu_text)
    
    if show_back and option == '0':
        print('Back')
        return ussd_menu(False)
    
    if option == '1':
        recipient_number = ask_question('0. Back\nEnter recipient 10-digit number: ' if current_language == 'en' else '0. Retour\nEntrez le numéro de 10 chiffres du destinataire: ')
        if recipient_number == '0':
            return ussd_menu(True)
        if not recipient_number.isdigit() or len(recipient_number) != 10:
            print('Invalid number.' if current_language == 'en' else 'Numéro invalide.')
            return ussd_menu(True)
        
        amount = ask_question('0. Back\nEnter amount (>=100): ' if current_language == 'en' else '0. Retour\nEntrez le montant (>=100): ')
        if amount == '0':
            return ussd_menu(True)
        try:
            amt = int(amount)
            if amt < 100:
                print('Invalid amount.' if current_language == 'en' else 'Montant invalide.')
                return ussd_menu(True)
            
            reason = ask_question('Enter reason for the amount: ' if current_language == 'en' else 'Entrez la raison du montant: ')
            secret_code = ask_question('Enter secret code (4 digits): ' if current_language == 'en' else 'Entrez le code secret (4 chiffres): ')
            if len(secret_code) != 4 or not secret_code.isdigit():
                print('Invalid secret code. It must be exactly 4 digits.' if current_language == 'en' else 'Code secret invalide. Il doit comporter exactement 4 chiffres.')
                return ussd_menu(True)
            
            print('Transfer successful' if current_language == 'en' else 'Transfert réussi')
            exit()
        except ValueError:
            print('Invalid amount.' if current_language == 'en' else 'Montant invalide.')
        
    elif option == '2':
        plan_option = ask_question('0. Back\n1. Plan for my number\n2. Plan for another number\nChoose option: ' if current_language == 'en' else '0. Retour\n1. Plan pour mon numéro\n2. Plan pour un autre numéro\nChoisissez une option: ')
        if plan_option == '0':
            return ussd_menu(True)
        if plan_option == '1':
            sub_plan_option = ask_question('0. Back\n1. Internet\n2. Call\nChoose option: ' if current_language == 'en' else '0. Retour\n1. Internet\n2. Appel\nChoisissez une option: ')
            if sub_plan_option == '0':
                return ussd_menu(True)
            elif sub_plan_option == '1':
                internet_option = ask_question('0. Back\n1. 200 AR\n2. 500 AR\n3. 1000 AR\n4. 2000 AR\n5. 5000 AR\n6. 10000 AR\nChoose option: ' if current_language == 'en' else '0. Retour\n1. 200 AR\n2. 500 AR\n3. 1000 AR\n4. 2000 AR\n5. 5000 AR\n6. 10000 AR\nChoisissez une option: ')
                if internet_option == '0':
                    return ussd_menu(True)
                elif internet_option in ['1', '2', '3', '4', '5', '6']:
                    amounts = {
                        '1': '200 AR',
                        '2': '500 AR',
                        '3': '1000 AR',
                        '4': '2000 AR',
                        '5': '5000 AR',
                        '6': '10000 AR'
                    }
                    print(f'Internet plan of {amounts[internet_option]} purchased.' if current_language == 'en' else f'Plan Internet de {amounts[internet_option]} acheté.')
                    exit()
                else:
                    print('Invalid option.' if current_language == 'en' else 'Option invalide.')
                    return ussd_menu(True)
            elif sub_plan_option == '2':
                call_option = ask_question('0. Back\n1. 200 AR\n2. 500 AR\n3. 1000 AR\n4. 2000 AR\n5. 5000 AR\n6. 10000 AR\nChoose option: ' if current_language == 'en' else '0. Retour\n1. 200 AR\n2. 500 AR\n3. 1000 AR\n4. 2000 AR\n5. 5000 AR\n6. 10000 AR\nChoisissez une option: ')
                if call_option == '0':
                    return ussd_menu(True)
                elif call_option in ['1', '2', '3', '4', '5', '6']:
                    amounts = {
                        '1': '200 AR',
                        '2': '500 AR',
                        '3': '1000 AR',
                        '4': '2000 AR',
                        '5': '5000 AR',
                        '6': '10000 AR'
                    }
                    print(f'Call plan of {amounts[call_option]} purchased.' if current_language == 'en' else f'Plan d\'appel de {amounts[call_option]} acheté.')
                    exit()
                else:
                    print('Invalid option.' if current_language == 'en' else 'Option invalide.')
                    return ussd_menu(True)
            else:
                print('Invalid option.' if current_language == 'en' else 'Option invalide.')
                return ussd_menu(True)
        elif plan_option == '2':
            recipient_number = ask_question('0. Back\nEnter 10-digit number: ' if current_language == 'en' else '0. Retour\nEntrez le numéro de 10 chiffres: ')
            if recipient_number == '0':
                return ussd_menu(True)
            if not recipient_number.isdigit() or len(recipient_number) != 10:
                print('Invalid number.' if current_language == 'en' else 'Numéro invalide.')
                return ussd_menu(True)
            sub_plan_option = ask_question('0. Back\n1. Internet\n2. Call\nChoose option: ' if current_language == 'en' else '0. Retour\n1. Internet\n2. Appel\nChoisissez une option: ')
            if sub_plan_option == '0':
                return ussd_menu(True)
            elif sub_plan_option == '1':
                internet_option = ask_question('0. Back\n1. 200 AR\n2. 500 AR\n3. 1000 AR\n4. 2000 AR\n5. 5000 AR\n6. 10000 AR\nChoose option: ' if current_language == 'en' else '0. Retour\n1. 200 AR\n2. 500 AR\n3. 1000 AR\n4. 2000 AR\n5. 5000 AR\n6. 10000 AR\nChoisissez une option: ')
                if internet_option == '0':
                    return ussd_menu(True)
                elif internet_option in ['1', '2', '3', '4', '5', '6']:
                    amounts = {
                        '1': '200 AR',
                        '2': '500 AR',
                        '3': '1000 AR',
                        '4': '2000 AR',
                        '5': '5000 AR',
                        '6': '10000 AR'
                    }
                    print(f'Internet plan of {amounts[internet_option]} sent to {recipient_number}.' if current_language == 'en' else f'Plan Internet de {amounts[internet_option]} envoyé à {recipient_number}.')
                    exit()
                else:
                    print('Invalid option.' if current_language == 'en' else 'Option invalide.')
                    return ussd_menu(True)
            elif sub_plan_option == '2':
                call_option = ask_question('0. Back\n1. 200 AR\n2. 500 AR\n3. 1000 AR\n4. 2000 AR\n5. 5000 AR\n6. 10000 AR\nChoose option: ' if current_language == 'en' else '0. Retour\n1. 200 AR\n2. 500 AR\n3. 1000 AR\n4. 2000 AR\n5. 5000 AR\n6. 10000 AR\nChoisissez une option: ')
                if call_option == '0':
                    return ussd_menu(True)
                elif call_option in ['1', '2', '3', '4', '5', '6']:
                    amounts = {
                        '1': '200 AR',
                        '2': '500 AR',
                        '3': '1000 AR',
                        '4': '2000 AR',
                        '5': '5000 AR',
                        '6': '10000 AR'
                    }
                    print(f'Call plan of {amounts[call_option]} sent to {recipient_number}.' if current_language == 'en' else f'Plan d\'appel de {amounts[call_option]} envoyé à {recipient_number}.')
                    exit()
                else:
                    print('Invalid option.' if current_language == 'en' else 'Option invalide.')
                    return ussd_menu(True)
            else:
                print('Invalid option.' if current_language == 'en' else 'Option invalide.')
                return ussd_menu(True)
        else:
            print('Invalid option.' if current_language == 'en' else 'Option invalide.')
            return ussd_menu(True)
    
    elif option == '3':
        if free_messages <= 0:
            print('Daily message limit reached.' if current_language == 'en' else 'Limite quotidienne de messages atteinte.')
            return ussd_menu(True)
        else:
            msg = ask_question('0. Back\nEnter your message: ' if current_language == 'en' else '0. Retour\nEntrez votre message: ')
            if msg == '0':
                return ussd_menu(True)
            recipient_number = ask_question('Enter recipient 10-digit number: ' if current_language == 'en' else 'Entrez le numéro de 10 chiffres du destinataire: ')
            if recipient_number == '0':
                return ussd_menu(True)
            if not recipient_number.isdigit() or len(recipient_number) != 10:
                print('Invalid recipient number.' if current_language == 'en' else 'Numéro de destinataire invalide.')
                return ussd_menu(True)
            free_messages -= 1
            print('Message sent to', recipient_number, '. Remaining:', free_messages)
            if free_messages == 0:
                print('Daily message limit reached.' if current_language == 'en' else 'Limite quotidienne de messages atteinte.')
            exit()
    
    elif option == '4':
        recipient_number = ask_question('Enter recipient 10-digit number for beep: ' if current_language == 'en' else 'Entrez le numéro de 10 chiffres du destinataire pour le bip: ')
        if recipient_number == '0':
            return ussd_menu(True)
        if not recipient_number.isdigit() or len(recipient_number) != 10:
            print('Invalid recipient number.' if current_language == 'en' else 'Numéro de destinataire invalide.')
            return ussd_menu(True)
        print('Beep sent to', recipient_number)
        exit()
    
    elif option == '5':
        language_option = ask_question('0. Back\n1. English\n2. French\nChoose option: ' if current_language == 'en' else '0. Retour\n1. Anglais\n2. Français\nChoisissez une option: ')
        if language_option == '0':
            return ussd_menu(True)
        elif language_option == '1':
            current_language = 'en'
            print('Language set to English.')
            return ussd_menu(False)
        elif language_option == '2':
            current_language = 'fr'
            print('Langue définie sur le français.')
            return ussd_menu(False)
        else:
            print('Invalid option.' if current_language == 'en' else 'Option invalide.')
            return ussd_menu(True)
    
    else:
        print('Invalid option.' if current_language == 'en' else 'Option invalide.')
    
    ussd_menu(show_back)

ussd_menu(False)
