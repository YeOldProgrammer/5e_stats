def attack_propability(prof, attrib, damage):
    bab = prof + attrib


def parse_dice(dice_str):
    min = 0
    avg = 0
    max = 0

    exp_buffer = ''
    for exp_idx in range(len(dice_str)):
        if dice_str[exp_idx] in ('+', '-'):
            count = 0
            die_found = False
            dice_buffer = ''
            for dice_idx in range(len(exp_buffer)):
                if exp_buffer[dice_idx] == 'd':
                    count = int(exp_buffer)
                    dice_buffer = ''
                    die_found = True
                else:
                    dice_buffer = dice_buffer + exp_buffer[dice_idx]

            if die_found is True:
                die = int(dice_buffer)
                min = min + count
                avg = avg + (die / 2) + 0.5
                max = max + count * die
            else:
                mod = int(dice_buffer)
                min = min + mod
                avg = avg + mod
                max = max + mod

            exp_buffer = ''

        elif dice_str[exp_idx] == 'd' or isinstance(dice_str[exp_idx], int):
            exp_buffer = exp_buffer + dice_str[exp_idx]

    return min, max, avg