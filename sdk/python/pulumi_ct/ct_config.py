# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'CtConfigResult',
    'AwaitableCtConfigResult',
    'ct_config',
    'ct_config_output',
]

@pulumi.output_type
class CtConfigResult:
    """
    A collection of values returned by ctConfig.
    """
    def __init__(__self__, content=None, id=None, platform=None, pretty_print=None, rendered=None, snippets=None, strict=None):
        if content and not isinstance(content, str):
            raise TypeError("Expected argument 'content' to be a str")
        pulumi.set(__self__, "content", content)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if platform and not isinstance(platform, str):
            raise TypeError("Expected argument 'platform' to be a str")
        pulumi.set(__self__, "platform", platform)
        if pretty_print and not isinstance(pretty_print, bool):
            raise TypeError("Expected argument 'pretty_print' to be a bool")
        pulumi.set(__self__, "pretty_print", pretty_print)
        if rendered and not isinstance(rendered, str):
            raise TypeError("Expected argument 'rendered' to be a str")
        pulumi.set(__self__, "rendered", rendered)
        if snippets and not isinstance(snippets, list):
            raise TypeError("Expected argument 'snippets' to be a list")
        pulumi.set(__self__, "snippets", snippets)
        if strict and not isinstance(strict, bool):
            raise TypeError("Expected argument 'strict' to be a bool")
        pulumi.set(__self__, "strict", strict)

    @property
    @pulumi.getter
    def content(self) -> str:
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def platform(self) -> Optional[str]:
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="prettyPrint")
    def pretty_print(self) -> Optional[bool]:
        return pulumi.get(self, "pretty_print")

    @property
    @pulumi.getter
    def rendered(self) -> str:
        return pulumi.get(self, "rendered")

    @property
    @pulumi.getter
    def snippets(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "snippets")

    @property
    @pulumi.getter
    def strict(self) -> Optional[bool]:
        return pulumi.get(self, "strict")


class AwaitableCtConfigResult(CtConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return CtConfigResult(
            content=self.content,
            id=self.id,
            platform=self.platform,
            pretty_print=self.pretty_print,
            rendered=self.rendered,
            snippets=self.snippets,
            strict=self.strict)


def ct_config(content: Optional[str] = None,
              platform: Optional[str] = None,
              pretty_print: Optional[bool] = None,
              snippets: Optional[Sequence[str]] = None,
              strict: Optional[bool] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableCtConfigResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['content'] = content
    __args__['platform'] = platform
    __args__['prettyPrint'] = pretty_print
    __args__['snippets'] = snippets
    __args__['strict'] = strict
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('ct:index/ctConfig:ctConfig', __args__, opts=opts, typ=CtConfigResult).value

    return AwaitableCtConfigResult(
        content=__ret__.content,
        id=__ret__.id,
        platform=__ret__.platform,
        pretty_print=__ret__.pretty_print,
        rendered=__ret__.rendered,
        snippets=__ret__.snippets,
        strict=__ret__.strict)


@_utilities.lift_output_func(ct_config)
def ct_config_output(content: Optional[pulumi.Input[str]] = None,
                     platform: Optional[pulumi.Input[Optional[str]]] = None,
                     pretty_print: Optional[pulumi.Input[Optional[bool]]] = None,
                     snippets: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                     strict: Optional[pulumi.Input[Optional[bool]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[CtConfigResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
