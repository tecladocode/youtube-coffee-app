import matplotlib.pyplot as plt


def method_to_rating_bar(methods):
    figure = plt.figure()
    axes = figure.add_subplot()

    axes.bar(
        range(len(methods)),
        [method[1] for method in methods],
        tick_label=[method[0] for method in methods]
    )

    return figure


def method_to_count_used(methods):
    figure = plt.figure()
    axes = figure.add_subplot()

    axes.pie(
        [method[1] for method in methods],
        labels=[method[0] for method in methods],
        autopct="%1.1f%%"
    )

    return figure
