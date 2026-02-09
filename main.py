from pyscript import display, document
def tea(m):
    document.getElementById('out').innerHTML=" "
    reyes=document.getElementById('reyes').value
    reno=document.getElementById('reno').value
    medyes=document.getElementById('medyes').value
    medno=document.getElementById('medno').value
    gra=document.getElementById('gra').value
    sec=document.getElementById('sec').value

    lvl=gra+sec
    if reyes == "yes":
        if medyes == "yes":
            if lvl=="7e" or lvl=="8e" or lvl=="9r" or lvl=="10r" or lvl=="11l" or lvl=="12j":
                display(f'You are in Blue Bears', target='out')
            elif lvl=="7s" or lvl=="8t" or lvl=="9s" or lvl=="10s" or lvl=="11h":
                display(f'You are in Green Hornets', target='out')
            elif lvl=="7r" or lvl=="8j" or lvl=="9r" or lvl=="10t" or lvl=="12n":
                display(f'You are in Red Bulldogs', target='out')
            elif lvl=="7t" or lvl=="8s" or lvl=="9t" or lvl=="10e" or lvl=="11a":
                display(f'You are in Green Hornets', target='out')
            else:
                display(f'your class isnt listed yet', target='out')
        elif medno == no:
            display(f'Get a medical certificate', target='out')
    elif reno == no:
        display(f'Get registered online', target='out')