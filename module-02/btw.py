def berekenbtw(bedrag_excl: float) -> float:
    return bedrag_excl * 1.21


bedrag = float(input('wat is het bedrag zonder btw? '))
incl_btw = (berekenbtw(bedrag))

print(f'het bedrag met btw is {incl_btw}')

