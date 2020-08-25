from MRR.simulator import MRR
from MRR.gragh import plot
from importlib import import_module
import argparse
from MRR.model import Model
from random import seed
from MRR.evaluator import Evaluator
from MRR.ring import Ring
from MRR.logger import Logger
from copy import deepcopy


def main(config):
    seed(1)
    model = Model(config)
    model.train()


def simulate(config_list):
    logger = Logger()
    xs = []
    ys = []

    for config in config_list:
        mrr = MRR(
            config['L'],
            config['K'],
            config
        )
        mrr.print_parameters()
        number_of_rings = len(config['L'])
        if 'lambda' in config:
            x = config['lambda']
        else:
            ring = Ring({
                'center_wavelength': config['center_wavelength'],
                'number_of_rings': number_of_rings,
                'n_eff': config['n_eff'],
                'n_eq': config['n_eq']
            })
            N = ring.calculate_N(config['L'])
            FSR = ring.calculate_practical_FSR(N)
            x = ring.calculate_x(FSR)

        y = mrr.simulate(x)
        config.setdeault('max_loss_in_pass_band', -10)
        config.setdeault('required_loss_in_stop_band', -20)
        config.setdeault('length_of_3db_band', 1e-9)

        evaluator = Evaluator(
            x,
            y,
            config
        )
        result = evaluator.evaluate_band()
        print(result)
        logger.save_data_as_csv(x, y, config['name'])
        xs.append(deepcopy(x))
        ys.append(deepcopy(y))
    print(xs[0].size)
    plot(xs, ys, config['L'].size, logger.generate_image_path(config['name']))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='config file path', nargs='*')
    args = vars(parser.parse_args())
    if args['config']:
        try:
            config_list = []
            for c in args['config']:
                config = import_module('config.simulate.{}'.format(c)).config
                config['name'] = c
                config_list.append(config)
        except:
            parser.print_help()
        else:
            simulate(config_list)
    else:
        try:
            config = import_module('config.base').config
        except:
            parser.print_help()
        else:
            main(config)
