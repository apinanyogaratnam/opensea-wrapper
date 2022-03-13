from opensea_wrapper.wrapper import get_collection


def main():
    """
    Main function to run the example
    """
    # Get the collection
    collection = 'cryptopunks'
    collection_data = get_collection(collection)

    return collection_data


if __name__ == '__main__':
    print(main())
