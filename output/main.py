from  output import serials
from output import netflix
from output import films

def main():
    serials_ = serials.serials()
    serials_.output(serials_.init_random_value())

    # netflix_ = netflix.netflix()
    # netflix_.output(netflix_.init_random_value())

    # films_ = films.films()
    # films_.output(films_.init_random_value())

main()