from LRModel import LRModel
import pandas as pd
from sys import argv, stderr
from time import sleep

# Something to iterate over...
models =    {
                "Gryffindor": LRModel(13, "Gryffindor"),
                "Hufflepuff": LRModel(13, "Hufflepuff"),
                "Ravenclaw": LRModel(13, "Ravenclaw")
            }

def main():
    if len(argv) != 2:
        stderr.write("usage: python3 logreg_train.py dataset_train.csv\n")
        exit(1)

    df = pd.read_csv(argv[1])
    df = df.drop(["Index", "First Name", "Last Name", "Birthday", "Best Hand"], 1)

    for model_feature in models:
        print("Training model {0}".format(model_feature))
        models[model_feature].train_model(df)
        print(models[model_feature].weights)

if __name__ == "__main__":
    main()

#float 	ft_compute_grad(t_env *env, int layer, int i, int j)
#{
#	float 	a;
#	float 	dzw;
#	float 	daz;
#	float	dca;
#	float 	pre_ret;
#
#	a = env->nw[layer][i].output;
#	dzw = env->nw[layer - 1][j].output;
#	daz = a * (1 - a);
#	dca = 2 * (a - env->target[i]);
#	pre_ret = dzw * daz;
#	if (layer > 1)
#		env->next_target[i] += (pre_ret * env->nw[layer - 1][j].weights[i]);
#	return (pre_ret * dca);
#}
