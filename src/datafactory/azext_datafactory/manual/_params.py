# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azext_datafactory.action import (
    AddFactoryVstsConfiguration,
    AddFactoryGitHubConfiguration
)


def load_arguments(self, _):

    with self.argument_context('datafactory create') as c:
        c.argument('factory_vsts_configuration', options_list=['--vsts-config', '--factory-vsts-configuration'],
                   action=AddFactoryVstsConfiguration, nargs='+', help='Factory\'s VSTS repo information.',
                   arg_group='RepoConfiguration')
        c.argument('factory_git_hub_configuration',
                   options_list=['--github-config', '--factory-git-hub-configuration'],
                   action=AddFactoryGitHubConfiguration, nargs='+', help='Factory\'s GitHub repo information.',
                   arg_group='RepoConfiguration')

    with self.argument_context('datafactory configure-factory-repo') as c:
        c.argument('factory_vsts_configuration', options_list=['--vsts-config', '--factory-vsts-configuration'],
                   action=AddFactoryVstsConfiguration, nargs='+', help='Factory\'s VSTS repo information.',
                   arg_group='RepoConfiguration')
        c.argument('factory_git_hub_configuration',
                   options_list=['--github-config', '--factory-git-hub-configuration'],
                   action=AddFactoryGitHubConfiguration, nargs='+', help='Factory\'s GitHub repo information.',
                   arg_group='RepoConfiguration')
