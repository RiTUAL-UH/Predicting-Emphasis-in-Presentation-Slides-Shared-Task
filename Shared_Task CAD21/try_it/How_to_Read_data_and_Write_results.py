
def read_data(filename):
    """
    This function reads the data from .txt file.
    :param filename: reading directory
    :return: lists of word_ids, words, emphasis probabilities
    """
    lines = read_lines(filename) + ['']
    word_id_lst, word_id_lsts =[], []
    post_lst, post_lsts = [], []
    bio_lst , bio_lsts = [], []
    freq_lst, freq_lsts = [], []
    e_freq_lst, e_freq_lsts = [], []
    
    for line in lines:
        if line:
            splitted = line.split("\t")
            word_id = splitted[0]
            words = splitted[1]
            bio= splitted[2]
            freq = splitted[3]
            e_freq = splitted[4]

            word_id_lst.append(word_id)
            post_lst.append(words)
            bio_lst.append(bio)
            freq_lst.append(freq)
            e_freq_lst.append(e_freq)

        elif post_lst:
            word_id_lsts.append(word_id_lst)
            post_lsts.append(post_lst)
            bio_lsts.append(bio_lst)
            freq_lsts.append(freq_lst)
            e_freq_lsts.append(e_freq_lst)
            word_id_lst =[]
            post_lst =[]
            bio_lst =[]
            freq_lst =[]
            e_freq_lst =[]
    return word_id_lsts, post_lsts, bio_lsts, freq_lsts, e_freq_lsts


def read_lines( filename):
    with open(filename, 'r') as fp:
        lines = [line.strip() for line in fp]
    return lines


def write_results(word_id_lsts, words_lsts, e_freq_lsts, write_to):
    """
    This function writes results in the format.
    :param word_id_lsts: list of word_ids
    :param words_lsts: list of words
    :param e_freq_lsts: lists of emphasis probabilities
    :param write_to: writing directory
    :return:
    """


    with open(write_to, 'w') as out:
        slide_id=""
        # a loop on all slides:
        for i in range(len(words_lsts)):
            # a loop on words in a slide:
            for j in range(len(words_lsts[i])):
                # writing:
                if slide_id ==i:
                    to_write = "{}\t{}\t{}\t".format(word_id_lsts[i][j], words_lsts[i][j], e_freq_lsts[i][j])
                    out.write(to_write + "\n")
                else:
                    out.write("\n")
                    to_write = "{}\t{}\t{}\t".format(word_id_lsts[i][j], words_lsts[i][j], e_freq_lsts[i][j])
                    out.write(to_write + "\n")
                    slide_id = i
        out.write("\n")
        out.close()




