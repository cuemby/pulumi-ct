# Ct Resource Provider

The Ct Resource Provider lets you manage [Ct](http://example.com) resources.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @pulumi/ct
```

or `yarn`:

```bash
yarn add @pulumi/ct
```

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi_ct
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/cuemby/pulumi-ct/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package Pulumi.Ct
```

## Configuration

The following configuration points are available for the `ct` provider:

- `ct:apiKey` (environment: `CT_API_KEY`) - the API key for `ct`
- `ct:region` (environment: `CT_REGION`) - the region in which to deploy resources

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/ct/api-docs/).
